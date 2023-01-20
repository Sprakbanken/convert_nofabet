import re

# Mapping dicts

PHONES = {
    "s": [("s", "S", "s"),],
    "h": [("h", "H", "h"),],
    "j": [("j", "J", "j"),],
    "v": [("v", "V", "v"), ("w", "W", "w")],
    "ng": [("N", "NG", "ŋ"),],
    "unvoiced_plosives": [("k", "K", "k"), ("p", "P", "p"), ("t", "T", "t"),],
    "voiced_plosives": [("b", "B", "b"), ("d", "D", "d"), ("g", "G", "g"),],
    "retroflex_plosives": [("d`", "RD", "ɖ"), ("t`", "RT", "ʈ")],
    "fricatives": [
        ("f", "F", "f"),
        ("S", "SJ", "ʃ"),
        ("C", "KJ", "ç"),
        ("s`", "RS", "ʂ"),
    ],
    "liquids": [("l", "L", "l"), ("r", "R", "r"), ("l`", "RL", "ɭ"),],
    "nasals": [("m", "M", "m"), ("n", "N", "n"), ("n`", "RN", "ɳ"),],
    "long_vowels": [
        ("A:", "AA", "ɑː"),
        ("{:", "AE", "æː"),
        ("e:", "EE", "eː"),
        ("i:", "II", "ɪː"),
        ("u:", "OO", "uː"),
        ("o:", "OA", "oː"),
        ("2:", "OE", "øː"),
        ("}:", "UU", "ʉː"),
        ("y:", "YY", "yː"),
    ],
    "short_vowels": [
        ("{", "AEH", "æ"),
        ("A", "AH", "ɑ"),
        ("@", "AX", "ə"),
        ("E", "EH", "ɛ"),
        ("I", "IH", "ɪ"),
        ("O", "OAH", "ɔ"),
        ("9", "OEH", "œ"),
        ("U", "OH", "ʊ"),
        ("u0", "UH", "ʉ"),
        ("Y", "YH", "ʏ"),
    ],
    "diphthongs": [
        ("{*I", "AEJ", "æ͡ɪ"),
        ("E*u0", "AEW", "æ͡ʉ"),
        ("A*I", "AJ", "ɑ͡ɪ"),
        ("9*Y", "OEJ", "œ͡ʏ"),
        ("O*Y", "OAJ", "ɔ͡ʏ"),
        ("O*Y", "OJ", "ɔ͡ʏ"),  # error. issue 17 in Rulebook
        ("@U", "OU", "o͡ʊ"),
    ],
    "consonant_nuclei": [
        ("l=", "LX", "l̩"),
        ("m=", "MX", "m̩"),
        ("n=", "NX", "n̩"),
        ("l`=", "RLX", "ɭ̩"),
        ("n`=", "RNX", "ɳ̩"),
        ("r=", "RX", "r̩"),
        ("s=", "SX", "s̩"),
    ],
}

NOFABET_TO_SAMPA_MAP = {x[1]: x[0] for y in PHONES.values() for x in y}
NOFABET_TO_SAMPA_MAP["0"] = ""
NOFABET_TO_SAMPA_MAP["1"] = '"'
NOFABET_TO_SAMPA_MAP["2"] = '""'
NOFABET_TO_SAMPA_MAP["3"] = "%"
NOFABET_TO_SAMPA_MAP["_"] = "_"
NOFABET_TO_SAMPA_MAP["$"] = "$"


NOFABET_TO_IPA_MAP = {x[1]: x[2] for y in PHONES.values() for x in y}
NOFABET_TO_IPA_MAP["0"] = ""
NOFABET_TO_IPA_MAP["1"] = "'"
NOFABET_TO_IPA_MAP["2"] = '"'
NOFABET_TO_IPA_MAP["3"] = "ˌ"
NOFABET_TO_IPA_MAP["_"] = "_"
NOFABET_TO_IPA_MAP["$"] = "."


PHONES["consonants"] = [
    x
    for x in [
        y
        for k in [
            "s",
            "h",
            "j",
            "v",
            "ng",
            "unvoiced_plosives",
            "voiced_plosives",
            "retroflex_plosives",
            "fricatives",
            "liquids",
            "nasals",
        ]
        for y in PHONES[k]
    ]
]

PHONES["long_nuclei"] = [
    x for x in [y for k in ["long_vowels", "diphthongs",] for y in PHONES[k]]
]

PHONES["short_nuclei"] = [
    x for x in [y for k in ["short_vowels", "consonant_nuclei",] for y in PHONES[k]]
]

PHONES["nuclei"] = [
    x for x in [y for k in ["short_nuclei", "long_nuclei",] for y in PHONES[k]]
]

PHONES["single_onsets"] = [
    x
    for x in [
        y
        for k in [
            "s",
            "h",
            "j",
            "v",
            "unvoiced_plosives",
            "voiced_plosives",
            "retroflex_plosives",
            "fricatives",
            "liquids",
            "nasals",
        ]
        for y in PHONES[k]
    ]
]

PHONES["sonor_consonants"] = [
    x for x in [y for k in ["j", "v", "ng", "liquids", "nasals"] for y in PHONES[k]]
]


PHONES_NOFABET = {k: [x[1] for x in v] for k, v in PHONES.items()}
PHONES_SAMPA = {k: [x[0] for x in v] for k, v in PHONES.items()}


# Functions


def is_valid_ons_cluster(phonelist):
    """Check if a list of NOFABET phones form a valid onset cluster in Norwegian"""
    is_valid = False
    if len(phonelist) == 2:
        if phonelist[0] in PHONES_NOFABET["nasals"]:
            if phonelist[1] == PHONES_NOFABET["j"]:
                is_valid = True
        elif phonelist[0] in ["P", "B"]:
            if phonelist[1] in PHONES_NOFABET["liquids"] + PHONES_NOFABET["j"]:
                is_valid = True
        elif phonelist[0] in ["T", "D"] + PHONES_NOFABET["retroflex_plosives"]:
            if phonelist[1] in ["R", "J"] + PHONES_NOFABET["v"]:
                is_valid = True
        elif phonelist[0] == "K":
            if phonelist[1] in PHONES_NOFABET["liquids"] + ["N"] + PHONES_NOFABET["v"]:
                is_valid = True
        elif phonelist[0] == "G":
            if phonelist[1] in PHONES_NOFABET["liquids"] + ["N"]:
                is_valid = True
        elif phonelist[0] == "F":
            if phonelist[1] in PHONES_NOFABET["liquids"] + PHONES_NOFABET["j"] + ["N"]:
                is_valid = True
        elif phonelist[0] in ["S", "SJ", "RS"]:
            if (
                phonelist[1]
                in PHONES_NOFABET["nasals"]
                + ["L"]
                + PHONES_NOFABET["v"]
                + PHONES_NOFABET["unvoiced_plosives"]
            ):
                is_valid = True
        elif phonelist[0] in PHONES_NOFABET["v"]:
            if phonelist[1] == "R":
                is_valid = True
        return is_valid
    elif len(phonelist) == 3:
        if phonelist[0] in ["S", "SJ", "RS"]:
            if phonelist[1] in ["P", "B"]:
                if phonelist[2] in ["L", "R", "J"]:
                    is_valid = True
            elif phonelist[1] in ["T", "D"]:
                if phonelist[2] in ["R", "J"]:
                    is_valid = True
            if phonelist[1] in ["K", "G"]:
                if phonelist[2] in ["L", "R", "V"]:
                    is_valid = True
        return is_valid
    else:
        return False


def get_item(mylist, index):
    try:
        return mylist[index]
    except IndexError:
        return None


def nofabet_to_syllables(transcription):
    """Convert a nofabet transcription to a list of syllables"""
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
        l = len(seglist)
        if start < 0:
            start = 0
        if end > l + 1:
            end = l + 1
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


def convert_nofabet(nofabet_transcription, to="sampa"):
    """Convert a NOFABET transcription to X-SAMPA (to='sampa') or IPA (to='ipa')"""
    nuc_pattern = re.compile("([A-Z]+)([0-3])")
    segs = []
    syllables = nofabet_to_syllables(nofabet_transcription)
    for i, syll in enumerate(syllables):
        tone = ""
        for phone in syll:
            if nuc_pattern.match(phone):
                tone = nuc_pattern.match(phone).group(2)
                segs.append(tone)
        for phone in syll:
            if nuc_pattern.match(phone):
                segs.append(nuc_pattern.match(phone).group(1))
            else:
                segs.append(phone)
        if i != len(syllables) - 1:
            segs.append("$")
    if to == "sampa":
        return "".join([NOFABET_TO_SAMPA_MAP[x] for x in segs])
    elif to == "ipa":
        return "".join([NOFABET_TO_IPA_MAP[x] for x in segs])
    else:
        raise Exception(f"{to} is an unknown standard")


if __name__ == "__main__":
    print(convert_nofabet("B IH2 L IH0 H EE0 T S AEH0 R S T AH3 T N IH0 NG G AX0 N S"))
    print(
        convert_nofabet(
            "B IH2 L IH0 H EE0 T S AEH0 R S T AH3 T N IH0 NG G AX0 N S", to="ipa"
        )
    )

