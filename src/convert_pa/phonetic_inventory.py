"""
Module with the phonetic inventory for Norwegian in three phonetic notations:
X-SAMPA,
Norwegian phonetic alphabet (Nofabet),
International phonetic alphabet (IPA)

Author: Per Erik Solberg
Maintainer: Ingerid Løyning Dale
License: Public domain (CC0)
"""

# All consonants, vowels and diphthongs in the NST lexicon. Values are lists of triplets, where the first element is
# the X-SAMPA form, the second the NoFAbet form, and the third the IPA form.
# The IPA transcription is mostly faithful to the X-SAMPA, except that E*u0 is æ͡ʉ, not ɛ͡ʉ and @U is ɔ͡ʊ, not ə͡ʊ
PHONETIC_ALPHABETS_MAP = {
    "consonants": [
        ("b", "B", "b"),
        ("d", "D", "d"),
        ("f", "F", "f"),
        ("g", "G", "g"),
        ("h", "H", "h"),
        ("j", "J", "j"),
        ("k", "K", "k"),
        ("C", "KJ", "ç"),
        ("l", "L", "l"),
        ("m", "M", "m"),
        ("n", "N", "n"),
        ("N", "NG", "ŋ"),
        ("p", "P", "p"),
        ("r", "R", "r"),
        ("d`", "RD", "ɖ"),
        ("l`", "RL", "ɭ"),
        ("n`", "RN", "ɳ"),
        ("s`", "RS", "ʂ"),
        ("t`", "RT", "ʈ"),
        ("s", "S", "s"),
        ("S", "SJ", "ʃ"),
        ("t", "T", "t"),
        ("v", "V", "v"),
        ("w", "W", "w"),
    ],
    "vowels": [
        ("A:", "AA", "ɑː"),
        ("{:", "AE", "æː"),
        ("{", "AEH", "æ"),
        ("A", "AH", "ɑ"),
        ("@", "AX", "ə"),
        ("e:", "EE", "eː"),
        ("E", "EH", "ɛ"),
        ("I", "IH", "ɪ"),
        ("i:", "II", "ɪː"),
        ("l=", "LX", "l̩"),
        ("m=", "MX", "m̩"),
        ("n=", "NX", "n̩"),
        ("o:", "OA", "oː"),
        ("O", "OAH", "ɔ"),
        ("2:", "OE", "øː"),
        ("9", "OEH", "œ"),
        ("U", "OH", "ʊ"),
        ("u:", "OO", "uː"),
        ("l`=", "RLX", "ɭ̩"),
        ("n`=", "RNX", "ɳ̩"),
        ("r=", "RX", "r̩"),
        ("s=", "SX", "s̩"),
        ("u0", "UH", "ʉ"),
        ("}:", "UU", "ʉː"),
        ("Y", "YH", "ʏ"),
        ("y:", "YY", "yː"),
    ],
    "diphthongs": [
        ("{*I", "AEJ", "æ͡ɪ"),
        ("E*u0", "AEW", "æ͡ʉ"),
        ("A*I", "AJ", "ɑ͡ɪ"),
        ("9*Y", "OEJ", "œ͡ʏ"),
        ("O*Y", "OJ", "ɔ͡ʏ"),
        ("@U", "OU", "o͡ʊ"),
    ],
}

# X-SAMPA to IPA mapping of syllable-pertaining symbols.
SYLL_CHAR_MAP = {
    "$": ".",  # syllable boundary
    "_": "_",  # word boundary in multiword expressions
    "¤": "¤",  # Guess: "¤" marks the word with the main phrasal stress in multiword expressions
    '"""': '"',  # indicates stressed syllable with tone 2
    '""': '"',  # stressed syllable with tone 2
    '"': "ˈ",  # stressed syllable with tone 1
    "%": "ˌ",  # secondary stress
}


SAMPA_TO_IPA_MAP = {
    seg[0]: seg[2]
    for segtypelist in PHONETIC_ALPHABETS_MAP.values()
    for seg in segtypelist
}


PHONES = {
    "s": [("s", "S", "s")],
    "h": [("h", "H", "h")],
    "j": [("j", "J", "j")],
    "v": [("v", "V", "v"), ("w", "W", "w")],
    "ng": [("N", "NG", "ŋ")],
    "unvoiced_plosives": [
        ("k", "K", "k"),
        ("p", "P", "p"),
        ("t", "T", "t"),
    ],
    "voiced_plosives": [
        ("b", "B", "b"),
        ("d", "D", "d"),
        ("g", "G", "g"),
    ],
    "retroflex_plosives": [("d`", "RD", "ɖ"), ("t`", "RT", "ʈ")],
    "fricatives": [
        ("f", "F", "f"),
        ("S", "SJ", "ʃ"),
        ("C", "KJ", "ç"),
        ("s`", "RS", "ʂ"),
    ],
    "liquids": [
        ("l", "L", "l"),
        ("r", "R", "r"),
        ("l`", "RL", "ɭ"),
    ],
    "nasals": [
        ("m", "M", "m"),
        ("n", "N", "n"),
        ("n`", "RN", "ɳ"),
    ],
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
    x
    for x in [
        y
        for k in [
            "long_vowels",
            "diphthongs",
        ]
        for y in PHONES[k]
    ]
]

PHONES["short_nuclei"] = [
    x
    for x in [
        y
        for k in [
            "short_vowels",
            "consonant_nuclei",
        ]
        for y in PHONES[k]
    ]
]

PHONES["nuclei"] = [
    x
    for x in [
        y
        for k in [
            "short_nuclei",
            "long_nuclei",
        ]
        for y in PHONES[k]
    ]
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
