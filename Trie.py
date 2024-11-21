class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word):
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['*'] = True

    def search(self, word):
        node = self.trie
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return '*' in node  

    def starts_with(self, prefix):
        node = self.trie
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True
