class TrieNode:
    def __init__(self):
        # to trach which char(node) point to which next child 
        # we use dictonary(hashmap) to find the relation
        # serach is like - children['a'] - search in o(1) times
        self.children = {}
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # node pointer to root
        node = self.root
        for char in word:
            if char not in node.children:
                # if curr char in the word is not in children dictonary 
                # add a new TrieNode
                node.children[char] = TrieNode()

            # point to newly added char so root -> new_char
            node = node.children[char]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False

            node = node.children[char]
        return node.isEnd 


    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            
            node = node.children[ch]
        return True
        