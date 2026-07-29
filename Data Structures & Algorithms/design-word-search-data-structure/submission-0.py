class TrieNode:

    def __init__(self):
        self.children = {}
        self.isEnd = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:

        node = self.root

        for ch in word:

            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]

        node.isEnd = True

    def search(self, word: str) -> bool:

        def dfs(index, node):

            # Entire word processed
            if index == len(word):
                return node.isEnd

            ch = word[index]

            # Wildcard
            if ch == ".":

                # Try every child
                for child in node.children.values():

                    if dfs(index + 1, child):
                        return True

                return False

            # Normal character
            if ch not in node.children:
                return False

            return dfs(index + 1, node.children[ch])

        return dfs(0, self.root)