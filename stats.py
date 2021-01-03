from collections import Counter
conv = {
'y' : 'oral_vowel ',
'E' : 'oral_vowel ',
'*' : 'oral_vowel ',
'a' : 'oral_vowel ',
'e' : 'oral_vowel ',
'i' : 'oral_vowel ',
'O' : 'oral_vowel ',
'9' : 'oral_vowel ',
'2' : 'oral_vowel ',
'u' : 'oral_vowel ',
'o' : 'oral_vowel ',
'1' : 'nasal_vowel ',
'5' : 'nasal_vowel ',
'@' : 'nasal_vowel ',
'8' : 'semi_vowel ',
'j' : 'semi_vowel ',
'w' : 'semi_vowel ',
'p' : 'plosive ',
'b' : 'plosive ',
't' : 'plosive ',
'g' : 'plosive ',
'k' : 'plosive ',
'd' : 'plosive ',
'Z' : 'fricative ',
'v' : 'fricative ',
'z' : 'fricative ',
'S' : 'fricative ',
'f' : 'fricative ',
's' : 'fricative ',
'R' : 'liquid ',
'l' : 'liquid ',
'G' : 'nasal ',
'N' : 'nasal ',
'm' : 'nasal ',
'n' : 'nasal ',
}

with open('output.txt') as file:
    words = [word.split() for word in file.readlines()]

cv_syllables = sum([word[5].split('-') for word in words], [])
syllables = sum([word[4].split('-') for word in words], [])
det_syllables = ["".join([conv[s] for s in list(syl)]) for syl in syllables]

cv_stat = Counter(cv_syllables)
syl_stat = Counter(syllables)
det_stat = Counter(det_syllables)

print('The 15 most frequent syllabic structures in French expressed with ‘C’ and ‘V’ forms:')
for i, (struc, num) in enumerate(cv_stat.most_common(15)):
    print(f'{i+1}. {struc} - {num}')
print('The 15 most frequent syllabic structures in French expressed with macro-classe forms:')
for i, (struc, num) in enumerate(det_stat.most_common(15)):
    print(f'{i+1}. {struc} - {num}')
print('The 15 most frequent syllabic structures in French expressed by consonants and vowels:')
for i, (struc, num) in enumerate(syl_stat.most_common(15)):
    print(f'{i+1}. {struc} - {num}')