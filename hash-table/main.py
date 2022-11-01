'''Hash Table

Description: Are used to store [key-value] pairs, they are like arrays, but the
keys are not ordened. Unlike arrays, hash tables are fast for all of the follo
wing operations: finding values, adding new values, or removing values.

Big O: Average Case

Insert: O(1)
Deletion: O(1)
Access: O(1)
'''


WEIRD_PRIME = 31


class HashTable():
    def __init__(self, size=53) -> None:
        self.key_map = [None for _ in range(0, size)]


    def _hash(self, key):
        total = 0
        for i in range(0, min(len(key), 100)):
            char = key[i]
            value = ord(char) - 96
            total = (total * WEIRD_PRIME + value) % len(self.key_map)
        return total

    
    def set(self, key, value):
        idx = self._hash(key)
        if not self.key_map[idx]:
            self.key_map[idx] = []
        self.key_map[idx].append([key, value])


    def get(self, key):
        idx = self._hash(key)

        if self.key_map[idx]:
            for i, v in enumerate(range(0, len(self.key_map[idx]))):
                if self.key_map[idx][i][0] == key:
                    return self.key_map[idx][i][1]
        return None


    def values(self):
        values  = []

        for p in self.key_map:
            if p:
                for c in p:
                    if c:
                        values.append(c[1])

        return values


    def keys(self):
        values  = []

        for p in self.key_map:
            if p:
                for c in p:
                    if c:
                        values.append(c[0])

        return values


ht = HashTable(17)
ht.set('maroon', '#800000')
ht.set('yellow', '#FFFF00')
ht.set('olive', '#808000')
ht.set('a', '#809000')
ht.set('a', '#807000')
print(ht.key_map)
print(ht.get('a'))
print(ht.keys())