#!/usr/bin/env python
# coding=utf-8

# Author: Per Erik Solberg, National Library of Norway
# License: Public domain (CC0)

import re
import sys

# Dict with all consonants, vowels and diphthongs in the NST lexicon. Values are lists of triplets, where the first element is
# the X-SAMPA form, the second the NoFAbet form (not relevant here), and the third the IPA form.
# The IPA transcription is mostly faithful to the X-SAMPA, except that E*u0 is æ͡ʉ, not ɛ͡ʉ and @U is ɔ͡ʊ, not ə͡ʊ
segdict = {'consonants': [('b', 'B', 'b'), ('d', 'D', 'd'), ('f', 'F', 'f'), ('g', 'G', 'g'), ('h', 'H', 'h'), ('j', 'J', 'j'), ('k', 'K', 'k'), \
                ('C', 'KJ', 'ç'), ('l', 'L', 'l'), ('m', 'M', 'm'), ('n', 'N', 'n'), ('N', 'NG', 'ŋ'), ('p', 'P', 'p'), ('r', 'R', 'r'), \
                ('d`', 'RD', 'ɖ'), ('l`', 'RL', 'ɭ'), ('n`', 'RN', 'ɳ'), ('s`', 'RS', 'ʂ'), ('t`', 'RT', 'ʈ'), ('s', 'S', 's'), ('S', 'SJ', 'ʃ'), \
                ('t', 'T', 't'), ('v', 'V', 'v'), ('w', 'W', 'w')], \
            'vowels': [('A:', 'AA', 'ɑː'), ('{:', 'AE', 'æː'), ('{', 'AEH', 'æ'), ('A', 'AH', 'ɑ'), ('@', 'AX', 'ə'), ('e:', 'EE', 'eː'), ('E', 'EH', 'ɛ'), \
                ('I', 'IH', 'ɪ'), ('i:', 'II', 'ɪː'), ('l=', 'LX', 'l̩'), ('m=', 'MX', 'm̩'), ('n=', 'NX', 'n̩'), ('o:', 'OA', 'oː'), ('O', 'OAH', 'ɔ'), ('2:', 'OE', 'øː'), \
                ('9', 'OEH', 'œ'), ('U', 'OH', 'ʊ'), ('u:', 'OO', 'uː'), ('l`=', 'RLX', 'ɭ̩'), ('n`=', 'RNX', 'ɳ̩'), ('r=', 'RX', 'r̩'), ('s=', 'SX', 's̩'), ('u0', 'UH', 'ʉ'), \
                ('}:', 'UU', 'ʉː'), ('Y', 'YH', 'ʏ'), ('y:', 'YY', 'yː')], \
            'diphthongs': [('{*I', 'AEJ', 'æ͡ɪ'), ('E*u0', 'AEW', 'æ͡ʉ'), ('A*I', 'AJ', 'ɑ͡ɪ'), ('9*Y', 'OEJ', 'œ͡ʏ'), ('O*Y', 'OJ', 'ɔ͡ʏ'), ('@U', 'OU', 'ɔ͡ʊ')]}
sampa_to_ipa_mapping = {seg[0]:seg[2] for segtypelist in segdict.values() for seg in segtypelist}

# X-SAMPA to IPA mapping of syllable-pertaining symbols. '$'/'.' is syllable boundary, '_' is word boundary in multiword expressions,
# '"""' or '""'/'"' indicates stressed syllable with tone 2, '"'/'ˈ' indicates stressed syllable with tone 1 and '%'/'ˌ' secondary stress.
# I think "¤" marks the word with the main phrasal stress in multiword expressions.
syllcharmapping = {'$': '.', '_': '_', '¤': '¤', '"""': '"', '""': '"', '"': 'ˈ', '%': 'ˌ'}

# Mapping from X-SAMPA segments and syllable-pertaining symbols to IPA
fullmapping = {**sampa_to_ipa_mapping, **syllcharmapping}

def _sampaparser(inputstring):
    totalpattern = re.compile(r'([bfghjkCNpSvw\$%¤_]|@(?!U)|[dt](?!`)|[sln](?![`=])|[mr](?!=)|[A{](?![:\*])|[O9E](?!\*)|(?<!\*)[IY]|(?<!@)U(?!:)|(?<!\")\"(?!\")|[dlnst]`(?!=)|[Aeio\{\}2uy]:|@U|\"{2}(?!\")|[lmnrs]=|(?<!\*)u0|_¤|[ln]`=|[\{A9O]\*[IY]|\"{3}|E\*u0)')
    returnstring = totalpattern.sub(r'\g<1> ', inputstring)
    return returnstring[:-1]

def sampa_to_ipa(inputstring):
    """Takes an input string in NST-style X-SAMPA and returns an output string in IPA"""
    parsed = _sampaparser(inputstring)
    sampalist = parsed.split(' ')
    ipastring = ''
    for el in sampalist:
        if not el in fullmapping.keys():
            sys.exit(f"The input string {inputstring} contains {el}, which is not a defined X-SAMPA segment")
        else:
            ipastring += fullmapping[el]
    return ipastring


if __name__ == "__main__":
    #test
    transcription = '""On$d@$%lE*u0s'
    print(sampa_to_ipa(transcription))