words = [x.strip().split() for x in open('files/Input_File.txt').readlines()]

symbols = set(sum([list(word[0]) for word in words], []))
phonemes = set(sum([list(word[1]) for word in words], []))

all_symbols = set('p t k b d g f s c v z g j m n r l h ç x w q a e i o u y é è ê î ô â ê ë ï à ù û'.split())
all_phonemes = set('p t k b d g f s S v z Z R l m n N G w j 8 a e i u o y E 9 2 O * @ 1 5'.split())

print('Letters that are present in the list and not in the file:')
print(" ".join(symbols.difference(all_symbols)))
print('Phonemes that are present in the list and not in the file:')
print(" ".join(phonemes.difference(all_phonemes)))
print('Letters that are present in the file and not in the list:')
print(" ".join(all_symbols.difference(symbols)))
print('Phonemes that are present in the file and not in the list:')
print(" ".join(all_phonemes.difference(phonemes)))
