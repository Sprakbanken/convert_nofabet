# Convert Phonetic Alphabets

Python package for converting phonetic or phonemic transcriptions from Nofabet to [IPA](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet) and [X-SAMPA](https://en.wikipedia.org/wiki/X-SAMPA), and from X-SAMPA to IPA (original code from https://github.com/peresolb/sampa_to_ipa).


## Installation 

```raw
pip install convert-pa
```

## Usage 


```python
# Convert from Nofabet
from convert_pa.convert_nofabet import convert_nofabet

test = "B IH2 L IH0 H EE0 T S AEH0 R S T AH3 T N IH0 NG G AX0 N S"

# to X-SAMPA 
print(convert_nofabet(test))
# '""bI$lI$he:t$s{r$%stAt$nIN$g@ns'

# to IPA
print(convert_nofabet(test, to="ipa"))
# '"bɪ.lɪ.heːt.sær.ˌstɑt.nɪŋ.gəns'

```

```python 
# Convert from X-SAMPA to IPA
from convert_pa.convert_sampa import sampa_to_ipa

transcription = '""On$d@$%lE*u0s'
print(sampa_to_ipa(transcription))
# "ɔn.də.ˌlæ͡ʉs
```