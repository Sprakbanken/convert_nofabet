#!/usr/bin/env python
# coding=utf-8

# Author: Per Erik Solberg, National Library of Norway
# License: Public domain (CC0)

import re

from convert_pa.phonetic_inventory import (
    NOFABET_TO_IPA_MAP,
    NOFABET_TO_SAMPA_MAP,
    PHONES_NOFABET,
    is_valid_ons_cluster,
    SAMPA_TO_IPA_MAP,
    SYLL_CHAR_MAP,
)


# Mapping from X-SAMPA segments and syllable-pertaining symbols to IPA
fullmapping = {**SAMPA_TO_IPA_MAP, **SYLL_CHAR_MAP}


def _sampaparser(inputstring):
    totalpattern = re.compile(
        r"([bfghjkCNpSvw\$%¤_]|@(?!U)|[dt](?!`)|[sln](?![`=])|[mr](?!=)|[A{](?![:\*])|[O9E](?!\*)|(?<!\*)[IY]|(?<!@)U(?!:)|(?<!\")\"(?!\")|[dlnst]`(?!=)|[Aeio\{\}2uy]:|@U|\"{2}(?!\")|[lmnrs]=|(?<!\*)u0|_¤|[ln]`=|[\{A9O]\*[IY]|\"{3}|E\*u0)"
    )
    returnstring = totalpattern.sub(r"\g<1> ", inputstring)
    return returnstring[:-1]


def sampa_to_ipa(inputstring):
    """Takes an input string in NST-style X-SAMPA and returns an output string in IPA"""
    if not inputstring:
        return ""
    trimmed = inputstring.replace(" ", "")
    parsed = _sampaparser(trimmed)
    sampalist = parsed.split(" ")
    ipastring = ""
    for el in sampalist:
        try:
            ipastring += fullmapping[el]
        except KeyError:
            raise ValueError(
                f"The input string {inputstring} contains '{el}', which is not a defined X-SAMPA segment"
            )
    return ipastring


def convert_nofabet_trans(nofabet_transcription: str, to: str = "ipa") -> str:
    """Convert a NOFABET transcription to X-SAMPA (to='sampa') or IPA (to='ipa')"""
    transcription = nofabet_transcription.lstrip().rstrip()
    nuc_pattern = re.compile("([A-Z]+)([0-3])")
    segs = []
    syllables = nofabet_to_syllables(transcription)
    for i, syll in enumerate(syllables):
        # first pass: gather all toneme markers
        segs += [
            match_obj.group(2)
            for phone in syll
            if (match_obj := nuc_pattern.match(phone))
        ]
        # second pass: gather phoneme
        segs += [
            match_obj.group(1) if (match_obj := nuc_pattern.match(phone)) else phone
            for phone in syll
        ]
        if i != len(syllables) - 1 and segs[-1] != "_":
            segs.append("$")
    if to == "sampa":
        return "".join([NOFABET_TO_SAMPA_MAP[x] for x in segs])
    elif to == "ipa":
        return "".join([NOFABET_TO_IPA_MAP[x] for x in segs])
    else:
        raise ValueError(
            f"`to=` should be either 'ipa' or 'sampa', got unknown notation: {to}"
        )


def nofabet_to_sampa(nofabet_transcription: str) -> str:
    return convert_nofabet_trans(nofabet_transcription, to="sampa")


def nofabet_to_ipa(nofabet_transcription: str) -> str:
    return convert_nofabet_trans(nofabet_transcription, to="ipa")


def nofabet_to_syllables(transcription: str) -> list:
    """Convert a nofabet transcription to a list of syllables."""
    if not transcription:
        return []
    nuclei = [x + str(i) for i in range(0, 4) for x in PHONES_NOFABET["nuclei"]]
    seglist = transcription.split(" ")
    syllables = []
    syll_list = []
    nucleus_found = False

    def checkout():
        nonlocal syllables
        nonlocal syll_list
        nonlocal nucleus_found
        syllables.append(syll_list)
        syll_list = []
        nucleus_found = False

    def context(n):
        nonlocal seglist
        try:
            return seglist[n]
        except IndexError:
            return None

    def context_range(start, end):
        nonlocal seglist
        length = len(seglist)
        if start < 0:
            start = 0
        if end > length + 1:
            end = length + 1
        return seglist[start:end]

    def is_last_syllable(n):
        nonlocal seglist
        is_last = True
        for seg in seglist[n + 1 : len(seglist)]:
            if seg in nuclei:
                is_last = False
        return is_last

    for i, seg in enumerate(seglist):
        syll_list.append(seg)
        if i == len(seglist) - 1:
            checkout()
            break
        if seg in nuclei:
            nucleus_found = True
            if context(i + 1) in nuclei:
                checkout()
            elif (
                context(i + 1) in PHONES_NOFABET["single_onsets"]
                and context(i + 2) in nuclei
            ):
                checkout()
            elif is_valid_ons_cluster(context_range(i + 1, i + 4)):
                checkout()
            elif is_valid_ons_cluster(context_range(i + 1, i + 3)):
                checkout()
        elif seg == "_":
            checkout()
        else:
            if nucleus_found and not is_last_syllable(i):
                if (
                    seg in PHONES_NOFABET["ng"]
                    and context(i - 1) in nuclei
                    and context(i + 1) in nuclei
                ):  # tang.en
                    checkout()
                elif is_valid_ons_cluster(context_range(i + 1, i + 4)):
                    checkout()
                elif is_valid_ons_cluster(context_range(i + 1, i + 3)):
                    checkout()
                elif (
                    seg in PHONES_NOFABET["consonants"]
                    and context(i + 1) in PHONES_NOFABET["consonants"]
                    and context(i + 2) in nuclei
                ):
                    checkout()
    return syllables
