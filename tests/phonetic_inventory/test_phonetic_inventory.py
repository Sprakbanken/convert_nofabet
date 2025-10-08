"""Check data integrity in the dictionaries used for converting between notation standards"""

from convert_pa import phonetic_inventory


def test_phonetic_alphabets_map_structure():
    # Check top-level keys
    assert "consonants" in phonetic_inventory.PHONETIC_ALPHABETS_MAP
    assert "vowels" in phonetic_inventory.PHONETIC_ALPHABETS_MAP
    assert "diphthongs" in phonetic_inventory.PHONETIC_ALPHABETS_MAP
    # Check that each entry is a list of triplets
    for _, val in phonetic_inventory.PHONETIC_ALPHABETS_MAP.items():
        assert isinstance(val, list)
        for triplet in val:
            assert isinstance(triplet, tuple)
            assert len(triplet) == 3
            for item in triplet:
                assert isinstance(item, str)


def test_sampa_to_ipa_map():
    # Check that all X-SAMPA keys map to correct IPA values
    for segtypelist in phonetic_inventory.PHONETIC_ALPHABETS_MAP.values():
        for xsampa, _, ipa in segtypelist:
            assert phonetic_inventory.SAMPA_TO_IPA_MAP[xsampa] == ipa


def test_nofabet_to_sampa_and_ipa_map():
    # Check that NoFAbet keys map to correct X-SAMPA and IPA values
    for segtypelist in phonetic_inventory.PHONETIC_ALPHABETS_MAP.values():
        for xsampa, nofabet, ipa in segtypelist:
            assert phonetic_inventory.NOFABET_TO_SAMPA_MAP[nofabet] == xsampa
            assert phonetic_inventory.NOFABET_TO_IPA_MAP[nofabet] == ipa


def test_phones_nofabet_and_sampa_consistency():
    # Ensure PHONES_NOFABET and PHONES_SAMPA have same keys and lengths
    assert set(phonetic_inventory.PHONES_NOFABET.keys()) == set(
        phonetic_inventory.PHONES_SAMPA.keys()
    )
    for key in phonetic_inventory.PHONES_NOFABET:
        assert len(phonetic_inventory.PHONES_NOFABET[key]) == len(
            phonetic_inventory.PHONES_SAMPA[key]
        )
