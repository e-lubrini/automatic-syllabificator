class FrenchWord:
    def __init__(self, word=''):
        self.word = word
        self.cv = self._get_cv()

    def _get_cv(self):
        # French (latin) alphabet characters
        # consonants = {'p', 't', 'k', 'b', 'd', 'g', 'f', 's', 'c', 'v', 'z', 'j', 'm', 'n', 'r', 'l', 'h'}
        vowels = {'a', 'à', 'e', 'é', 'ê', 'ë', 'i', 'ï', 'î', 'o', 'u', 'y', 'ù'}
        cv = ['V' if char in vowels else 'C' for char in self.word]
        return "".join(cv)


class SampaWord:
    def __init__(self, word, transcription):
        self.word = word
        self.transcription = transcription
        self.cv = self._get_cv()
        self.s_word = self._split_word()
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

        final_word = ''
        self.cv += '      '
        self.transcription += '      '
        self.s_word = list(self.transcription)
        plus_i = 0

        for i in range(len(self.s_word)):
            i += plus_i

            # 1 consonant between 2 vowels VCV  consonant in onset position of the second syllable;
            if self.cv[i:i + 3] == 'VCV':
                final_word += self.transcription[i] + '-'

            # 2 adjacent vowels VV  2 syllables;
            elif self.cv[i:i + 2] == 'VV':
                final_word += self.transcription[i] + '-'

            # 2 consonants between two vowels: VCCV
            elif self.cv[i:i + 4] == 'VCCV':
                # the first consonant is different from liquids and semi-vowels and the second is a liquid or a
                # semivowel  the whole consonant cluster in onset position of the next syllable (note: never
                # separate a consonant from a semivowel or a liquid). V-CCV
                if self.s_word[i + 1] not in [*liquids, *semi_vowels] and self.s_word[i + 2] in [*liquids,
                                                                                                 *semi_vowels]:
                    final_word += self.transcription[i] + '-' + self.transcription[i + 1:i + 4] + '-'
                    plus_i += 3

                # 2 liquids   syllabic boundary between the two liquids;
                # VC-CV
                elif self.s_word[i + 1] in [*liquids, *semi_vowels] and self.s_word[i + 2] in [*liquids, *semi_vowels]:
                    final_word += self.transcription[i:i + 2] + '-'
                    plus_i += 1

                # the first consonant is a liquid and a second is not a liquid neither a semi-vowel  syllabic
                # boundary between the two consonants. VC-CV
                elif self.s_word[i + 1] in liquids and self.s_word[i + 2] not in [*liquids, *semi_vowels]:
                    final_word += self.transcription[i:i + 2] + '-'
                    plus_i += 1

                # the first consonant is a semi-vowel and the second any consonant  syllabic boundary between the
                # semi-vowel and the second consonant. VC-CV
                elif self.s_word[i + 1] in semi_vowels:
                    final_word += self.transcription[i:i + 2] + '-'
                    plus_i += 1

                # the two adjacent consonants are neither liquids nor semi-vowel  syllabic boundary between the two
                # consonants. VC-CV
                if self.s_word[i + 1] not in [*liquids, *semi_vowels] and self.s_word[i + 2] not in [*liquids,
                                                                                                     *semi_vowels]:
                    final_word += self.transcription[i:i + 2] + '-'
                    plus_i += 1

            # 3 consonants between 2 vowels: VCCCV
            elif self.cv[i:i + 5] == 'VCCCV':
                # the first is not a liquid nor a semi-vowel, the second is a liquid and the third a semi-vowel  the
                # whole consonant cluster in onset position. V-CCCV
                if self.s_word[i + 1] not in [*liquids, *semi_vowels] and self.s_word[i + 2] in liquids and self.s_word[
                    i + 3] in semi_vowels:
                    final_word += self.transcription[i] + '-'


                # 3 consonants (or more): they are neither liquids nor semi-vowels  syllabic boundary between the
                # two first or two last consonants VC-CCV
                else:
                    final_word += self.transcription[i:i + 2] + '-'
                    plus_i += 1

            # 4 consonants between 2 vowels: V-CCCCV
            elif self.cv[i:i + 6] == 'VCCCCV':
                final_word += self.transcription[i] + '-' + self.transcription[i + 1:i + 5]
                plus_i += 4

            # 5 consonants between 2 vowels: V-CCCCCV
            elif self.cv[i:i + 7] == 'VCCCCCV':
                final_word += self.transcription[i] + '-' + self.transcription[i + 1:i + 6]
                plus_i += 5

            # 1 consonant + 1 vowel syllable: CV-
            elif self.cv[i:i + 4] == 'CVCV':
                final_word += self.transcription[i:i + 2] + '-'
                plus_i += 1

            # 1 consonant before the new syllable: C
            elif self.cv[i:i + 5] == 'CVCCV':
                final_word += self.transcription[i]

            # 1 consonant + 1 vowel syllable at the end of the word: -CV
            elif self.cv[i:i + 3] == 'CV ':
                if final_word:
                    if final_word[-1] != '-':
                        final_word += '-' + self.transcription[i:i + 2]
                    else:
                        final_word += self.transcription[i:i + 2]
                else:
                    final_word += self.transcription[i:i + 2]
                break

            # 1 consonant + 1 vowel + 1 consonant syllable at the end of the word: -CVC
            elif self.cv[i:i + 4] == 'CVC ':
                final_word += self.transcription[i:i + 3]
                break

            # 1 consonant at the end of the word: C
            elif self.cv[i:i + 2] == 'C ':
                if final_word:
                    if final_word[-1] == '-':
                        final_word = final_word[:-1] + self.transcription[i]
                    else:
                        final_word += self.transcription[i]
                else:
                    final_word += self.transcription[i]
                break

            # 2 consonants at the end of the word: CC
            elif self.cv[i:i + 3] == 'CC ':
                if final_word:
                    if final_word[-1] == '-':
                        final_word = final_word[:-1] + self.transcription[i:i + 2]
                    else:
                        final_word += self.transcription[i:i + 2]
                else:
                    final_word += self.transcription[i:i + 2]
                break

            # 2 consonants and a vowel at the end of the word: -CCV
            elif self.cv[i:i + 4] == 'CCV ':
                if final_word:
                    if self.cv[i - 1] != 'C' and self.cv[i - 2] != 'V':
                        if final_word[-1] != '-':
                            final_word += '-' + self.transcription[i:i + 3]
                        else:
                            final_word += self.transcription[i:i + 3]
                    else:
                        final_word += self.transcription[i:i + 3]
                else:
                    final_word += self.transcription[i:i + 3]
                break

            # end of the word
            elif self.s_word[i] == ' ':
                break

            # any other symbol that was not caught by the previous rules
            else:
                if final_word:
                    if self.cv[i] == 'C' and self.cv[i + 1] == 'C' and final_word[-1] == '-' and self.cv[
                        i - 1] != 'V' and self.cv[i - 2] != 'V':
                        final_word = final_word[:-1] + self.transcription[i]
                    else:
                        final_word += self.transcription[i]
                else:
                    final_word += self.transcription[i]
                continue

        return final_word.strip()[:-1] if final_word.endswith('-') else final_word.strip()

    def _get_cv(self):
        vowels = {'a', 'e', 'i', 'u', 'o', 'y', 'E', '9', '2', 'O', '*', '@', '1', '5'}
        cv = ['V' if char in vowels else 'C' for char in self.transcription]
        return "".join(cv)

    def _split_cv(self):
        vowels = {'a', 'e', 'i', 'u', 'o', 'y', 'E', '9', '2', 'O', '*', '@', '1', '5'}
        s_cv = ['V' if char in vowels else '-' if char == '-' else 'C' for char in self.s_word]
        return "".join(s_cv)


if __name__ == '__main__':
    words = [x.strip().split() for x in open('files/Input_File.txt').readlines()]
    words[0][0] = words[0][0][1:]
    with open('output.txt', 'w') as file:
        for word, trans in words:
            french = FrenchWord(word)
            sampa = SampaWord(word, trans)
            file.write(f'{word} {french.cv} {trans} {sampa.cv.strip()} {sampa.s_word} {sampa.s_cv}\n')
