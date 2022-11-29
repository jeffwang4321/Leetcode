class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode() # add TrieNode if it doesnt exist 
            cur = cur.children[c] # interate through Trie if it exits
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


# python3 '.\208. Implement Trie (Prefix Tree).py'
if __name__ == "__main__":
  trie = Trie()
  trie.insert("apple")
  print(trie.search("apple"))   # return True
  print(trie.search("app"))     # return False
  print(trie.startsWith("app")) # return True
  trie.insert("app")
  print(trie.search("app"))     # return True
  



