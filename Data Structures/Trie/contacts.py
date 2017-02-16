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

    def find_partial(self, match):
        current = self.items

        for letter in match:
            if current.get(letter):
                current = current[letter]
            else:
                return 0

        return current[self._count]


if __name__ == '__main__':
    n = int(stdin.readline())
    t = Trie()
    for _ in range(n):
        q = [w for w in stdin.readline().strip().split(' ')]
        if q[0] == 'add':
            t.add(q[1])
        elif q[0] == 'find':
            print(t.find_partial(q[1]))
