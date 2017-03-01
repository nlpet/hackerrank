from sys import stdin


class Trie:
    def __init__(self):
        self.items = {}
        self._end = '_end_'
        self._count = '_count_'

    def add(self, word):
        current = self.items
        for letter in word:
            current = current.setdefault(letter, {self._count: 0})
            current[self._count] += 1
        current[self._end] = self._end

        return self.items

    def find_prefixes(self):
        prefixes = []
        stack = [self.items]
        common_prefix = []

        while stack:
            current = stack.pop()
            letters = [
                k for k in current
                if k not in (self._end, self._count) and current[k][self._count] > 1
            ]

            for letter in letters:
                if not current[letter].get(self._end):
                    common_prefix.append(letter)
                    stack.append(current[letter])
                else:

            if len(letters) == 1 and not current[letters[0]].get(self._end):
                common_prefix.append(letters[0])
            else:
                pass



        # while stack:
        #     current = stack.pop()
        #     for letter in [k for k in current if k not in (self._end, self._count)]:
        #         if current[letter][self._count] > 1:
        #             if not current[letter].get(self._end):
        #                 common_prefix.append(letter)
        #             else:
        #                 prefixes.append(''.join(commmon_prefix) + letter)
        #             prefix.append(letter)
        #             stack.append(current[letter])
        #
        # if current.get(self._end):
        #     return ''.join(prefix)
        # return None

    def get_words_from_prefixes(self, prefixes):
        word, current = [], self.items

        for letter in prefix:
            current = current[letter]

        stack = [current]

        while stack:
            current = stack.pop()
            letter = [k for k in current if k not in (self._end, self._count)]
            if letter:
                word.append(letter[0])
                stack.append(current[letter[0]])

        return prefix + ''.join(word)

    def find_partial(self, match):
        current = self.items

        for letter in match:
            if current.get(letter):
                current = current[letter]
            else:
                return 0

        return current[self._count]


if __name__ == '__main__':
    N = int(stdin.readline())
    t = Trie()
    words = []

    for _ in range(N):
        s = stdin.readline().strip()
        words.append(s)
        t.add(s)

    prefixes = t.find_prefixes()

    if not prefixes:
        print('GOOD SET')
    else:
        print('BAD SET')
        prefixed_words = t.get_words_from_prefixes(prefixes)
        first_prefixed_word = len(words)
        for pw in prefixed_words:
            indx = words.index(pw)
            if indx < first_prefixed_word:
                first_prefixed_word = indx
        print(words.index(first_prefixed_word))
