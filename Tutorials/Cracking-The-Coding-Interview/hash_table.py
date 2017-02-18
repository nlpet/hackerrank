
class Node(object):
    def __init__(self, key=None, value=None, next_node=None):
        self.key = key
        self.value = value
        self.next_node = next_node

    @property
    def data(self):
        return (self.key, self.value)

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def _get_all(self, item_type):
        current = self.head
        items = []
        while current:
            items.append(current.__getattribute__(item_type))
            current = current.get_next()
        return items

    def insert(self, key, value):
        new_node = Node(key, value)
        new_node.set_next(self.head)
        self.head = new_node

    def search(self, key):
        current, found = self.head, False

        while current and not found:
            if current.key == key:
                found = True
            else:
                current = current.get_next()

        if current:
            return current.value

        return None

    def delete(self, key):
        current, previous, found = self.head, None, False

        while current and found is False:
            if current.key == key:
                found = True
            else:
                previous = current
                current = current.get_next()

        if current is None:
            raise KeyError(key)

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def get_all_keys(self):
        return self._get_all('key')

    def get_all_values(self):
        return self._get_all('value')


class HashTable:
    def __init__(self, size):
        self.size = size
        self._keys = [None] * size
        self._values = [None] * size

    def __getitem__(self, key):
        indx = self.__hash__(key)
        if isinstance(self._keys[indx], LinkedList):
            return self._keys[indx].search(key)
        else:
            return self._values[indx]

    def __setitem__(self, key, value):
        indx = self.__hash__(key)
        if self._keys[indx] is None:
            self._keys[indx] = key
            self._values[indx] = value
        else:
            if self._keys[indx] == key:
                self._values[indx] = value
            elif isinstance(self._keys[indx], LinkedList):
                self._keys[indx].insert(key, value)
            else:
                new_item = LinkedList()
                new_item.insert(self._keys[indx], self._values[indx])
                new_item.insert(key, value)
                self._keys[indx] = new_item
                self._values[indx] = new_item

    def __delitem__(self, key):
        indx = self.__hash__(key)
        if isinstance(self._keys[indx], LinkedList):
            self._keys[indx].delete(key)
        else:
            self._keys[indx] = None
            self._values[indx] = None

    def __repr__(self):
        return repr(self._get_set_pairs())

    def __hash__(self, key):
        if isinstance(key, str):
            return self._hash_string(key)
        elif isinstance(key, (int, float)):
            return self._hash_number(key)
        else:
            raise TypeError('Unhashable type: {}'.format(type(key)))

    def _hash_string(self, s):
        weighed_sum = 0
        for pos in range(len(s)):
            weighed_sum += ord(s[pos])
        return weighed_sum % self.size

    def _hash_number(self, n):
        return n ** 2 % self.size

    def _get_set_items(self, lst):
        return tuple(filter(lambda i: i is not None, lst))

    def _get_set_pairs(self):
        return list(
            zip(self._get_set_items(self._keys),
                self._get_set_items(self._values))
        )

    def keys(self):
        return self._get_set_items(self._keys)

    def values(self):
        return self._get_set_items(self._values)

    def items(self):
        return self._get_set_pairs()
