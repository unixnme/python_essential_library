class Trie(object):
    def __init__(self):
        self.data = {}

    def __getitem__(self, keys):
        result = self.data[keys[0]]
        if keys[1:]:
            result = result[keys[1:]]
        return result


    def __contains__(self, keys):
        if keys[0] not in self.data:
            return False
        if keys[1:]:
            element = self.data[keys[0]]
            if isinstance(element, Trie):
                return keys[1:] in element
            return False
        return True


    def __setitem__(self, keys, value):
        if len(keys) == 1:
            self.data[keys[0]] = value
        else:
            key = keys[0]
            if key not in self.data:
                self.data[key] = Trie()
                self.data[key][keys[1:]] = value
            else:
                self.data[key][keys[1:]] = value


import unittest
class TrieUnitTest(unittest.TestCase):
    def test_trie(self):
        trie = Trie()
        trie[[1,2,3]] = 1
        self.assertTrue([1,2,3] in trie)
        self.assertTrue(trie[[1,2,3]] == 1)

        trie[[1,2,3]] += 2
        self.assertTrue(trie[[1,2,3]] == 3)
        self.assertFalse([1,2,3,4] in trie)
        self.assertTrue([1,2] in trie)


        trie[1,2] = 3
        self.assertFalse([1, 2, 3] in trie)
        self.assertTrue([1, 2] in trie)
        self.assertTrue([1] in trie)