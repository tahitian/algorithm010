class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for a in word:
            if a not in node:
                node[a] = {}
            node = node[a]
        # 单词结束标志
        node["#"] = "#"

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for a in word:
            if a not in node:
                return False
            node = node[a]
        return "#" in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for a in prefix:
            if a not in node:
                return False
            node = node[a]
        return True