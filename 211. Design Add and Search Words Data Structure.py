class TrieNode:
    def __init__(self):
        self.children = {} # a : TrieNode
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word

        return dfs(0, self.root)


# python3 '.\211. Design Add and Search Words Data Structure.py'
if __name__ == "__main__":
  wordDictionary = WordDictionary()
  wordDictionary.addWord("bad")
  wordDictionary.addWord("dad")
  wordDictionary.addWord("mad")
  print(wordDictionary.search("pad")) # return False
  print(wordDictionary.search("bad")) # return True
  print(wordDictionary.search(".ad")) # return True
  print(wordDictionary.search("b..")) # return True
  



