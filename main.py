from collections import Counter
import pandas


class FrenchWord:
    def __init__(self, word=''):
        self.word = word
        self.cv = self._get_cv()

    def _get_cv(self):
        # French (latin) alphabet characters
        # consonants = {'p', 't', 'k', 'b', 'd', 'g', 'f', 's', 'c', 'v', 'z', 'j', 'm', 'n', 'r', 'l', 'h'}
        vowels = {'a', 'à', 'e', 'é', 'ê', 'ë', 'i', 'ï', 'o', 'u', 'y', 'ù'}
        for char in self.word:
            if char in vowels:
                self.cv.append('V')
            else:
                self.cv.append('C')

        return self.cv


class SampaWord:
    def __init__(self, word):
        self.word = word
        self.s_word = self._split_word()
        self.cv = self._get_cv()
        self.s_cv = self._split_cv()

    def _split_word(self):
        # SAMPA phonetic alphabet characters
        oral_vowels = {'a', 'e', 'i', 'u', 'o', 'y', 'E', '9', '2', 'O', '*'}
        nasal_vowels = {'@', '1', '5'}
        semi_vowels = {'w', 'j', '8'}
        plosives = {'p', 't', 'k', 'b', 'd', 'g'}
        fricatives = {'f', 's', 'S', 'v', 'z', 'Z'}
        liquids = {'R', 'l'}
        nasals = {'m', 'n', 'N', 'G'}

        vowels = [*oral_vowels, *nasal_vowels]
        consonants = [*semi_vowels, *plosives, *fricatives, *liquids, *nasals]

        self.s_word = list(self.word)

        for i, char in enumerate(list(self.word)):
            print(i, len(list(self.word)))
            #i = index(char)

            # 1 consonant between 2 vowels VCV  consonant in onset position of the second syllable;
            if self.s_word[i] in vowels and self.s_word[i + 1] in consonants and self.s_word[i + 2] in vowels:
                self.s_word[i:(i + 3)] = self.s_word[i] + '-' + "".join(self.s_word[i + 1:i + 3])


            # 2 adjacent vowels VV  2 syllables;
            elif self.s_word[i] in vowels and self.s_word[i + 1] in vowels:
                self.s_word[i:(i + 2)] = self.s_word[i] + '-' + self.s_word[i + 1]

            # 2 consonants between two vowels: VCCV
            elif self.s_word[i] in vowels and self.s_word[i + 1] in consonants and self.s_word[i + 2] in consonants and self.s_word[
                i + 3] in vowels:

                # the first consonant is different from liquids and semi-vowels and the second is a liquid or a
                # semivowel  the whole consonant cluster in onset position of the next syllable (note: never
                # separate a consonant from a semivowel or a liquid). V-CCV
                if self.s_word[i + 1] not in [*liquids, *semi_vowels] and self.s_word[i + 2] in [*liquids, *semi_vowels]:
                    self.s_word[i:i + 4] = self.s_word[i] + '-' + "".join(self.s_word[i + 1:i + 4])

                # 2 liquids   syllabic boundary between the two liquids;
                # VC-CV
                elif self.s_word[i + 1] in [*liquids, *semi_vowels] and self.s_word[i + 2] in [*liquids, *semi_vowels]:
                    self.s_word[i:i + 4] = "".join(self.s_word[i:i + 2]) + '-' + "".join(self.s_word[i + 2:i + 4])

                # the first consonant is a liquid and a second is not a liquid neither a semi-vowel  syllabic
                # boundary between the two consonants. VC-CV
                elif self.s_word[i + 1] in liquids and self.s_word[i + 2] not in [*liquids, *semi_vowels]:
                    self.s_word[i:i + 4] = "".join(self.s_word[i:i + 2]) + '-' + "".join(self.s_word[i + 2:i + 4])

                # the first consonant is a semi-vowel and the second any consonant  syllabic boundary between the
                # semi-vowel and the second consonant. VC-CV
                elif self.s_word[i + 1] in semi_vowels:
                    self.s_word[i:i + 4] = "".join(self.s_word[i:i + 2]) + '-' + "".join(self.s_word[i + 2:i + 4])

                # the two adjacent consonants are neither liquids nor semi-vowel  syllabic boundary between the two
                # consonants. VC-CV
                if self.s_word[i + 1] not in [*liquids, *semi_vowels] and self.s_word[i + 2] not in [*liquids, *semi_vowels]:
                    self.s_word[i:i + 4] = "".join(self.s_word[i:i + 2]) + '-' + "".join(self.s_word[i + 2:i + 4])

            # 3 consonants between 2 vowels: VCCCV
            elif self.s_word[i] in vowels and self.s_word[i + 1] in consonants and self.s_word[i + 2] in consonants and self.s_word[
                i + 3] in consonants and self.s_word[i + 4] in vowels:

                # the first is not a liquid nor a semi-vowel, the second is a liquid and the third a semi-vowel  the
                # whole consonant cluster in onset position. V-CCCV
                if self.s_word[i + 1] not in [*liquids, *semi_vowels] and self.s_word[i + 2] in liquids and self.s_word[i + 3] in semi_vowels:
                    self.s_word[i:i + 5] = self.s_word[i] + '-' + self.s_word[i + 1:i + 5]

                # 3 consonants (or more): they are neither liquids nor semi-vowels  syllabic boundary between the
                # two first or two last consonants VC-CCV
                else:
                    self.s_word[i:i + 5] = self.s_word[i:i + 2] + '-' + self.s_word[i + 2:i + 5]

            # continue if char is a dash '-'
            else:
                continue

        return self.s_word

    def _get_cv(self):

        vowels = {'a', 'e', 'i', 'u', 'o', 'y', 'E', '9', '2', 'O', '*', '@', '1', '5'}
        cv = ''
        for char in self.word:
            if char in vowels:
                cv += 'V'
            else:
                cv += 'C'

        return cv

    def _split_cv(self):

        vowels = {'a', 'e', 'i', 'u', 'o', 'y', 'E', '9', '2', 'O', '*', '@', '1', '5'}
        s_cv = ''
        for char in self.word:
            if char == '-':
                s_cv += '-'
            elif char in vowels:
                s_cv += 'V'
            else:
                s_cv += 'C'

        return s_cv


if __name__ == '__main__':
    #main()
    s = SampaWord('bouteille')
    print(s.cv)
    print(s.word)
    print(s.s_cv)
    print(s.s_word)
