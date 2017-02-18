from collections import Counter

def ransom_note(magazine, ransom):
    mag_words_counter = Counter(magazine)
    for word in ransom:
        if mag_words_counter.get(word, 0) > 0:
            mag_words_counter[word] -= 1
        else:
            return False
    return True

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)

if(answer):
    print("Yes")
else:
    print("No")
