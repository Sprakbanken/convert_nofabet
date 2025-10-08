# Convert Phonetic Alphabets

Python package for converting phonetic or phonemic transcriptions from Nofabet to [IPA](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet) and [X-SAMPA](https://en.wikipedia.org/wiki/X-SAMPA), and from X-SAMPA to IPA (original code from <https://github.com/peresolb/sampa_to_ipa>).

## Installation

```shell
pip install convert-pa
```

## Usage

```python
from convert_pa import nofabet_to_ipa, nofabet_to_sampa, sampa_to_ipa, nofabet_to_syllables

# Convert from Nofabet
nofabet_transcription = "B IH2 L IH0 H EE0 T S AEH0 R S T AH3 T N IH0 NG G AX0 N S"

# to IPA
print(nofabet_to_ipa(nofabet_transcription))
# '"bɪ.lɪ.heːt.sær.ˌstɑt.nɪŋ.gəns'

# to X-SAMPA 
print(nofabet_to_sampa(nofabet_transcription))
# '""bI$lI$he:t$s{r$%stAt$nIN$g@ns'

# Convert from X-SAMPA to IPA
sampa_transcription = '""On$d@$%lE*u0s'
print(sampa_to_ipa(sampa_transcription))
# "ɔn.də.ˌlæ͡ʉs

# Divide a nofabet transcription into syllables (list of lists of phonemes)
# Word: "Billigsalg"
nofabet_to_syllables("B IH2 L IH0 S AH1 L G ") 
# [['B', 'IH2'], ['L', 'IH0'], ['S', 'AH1', 'L', 'G', '']]
```
