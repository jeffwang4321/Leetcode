from typing import List

class TrieNode:
    def __init__(self):
        self.children = {} # key: char, TrieNode
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for w in words:
            root.addWord(w)
        
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or
                r == ROWS or c == COLS or
                (r, c) in visit or board[r][c] not in node.children):
                return
            
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            
            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)



# python3 '.\212. Word Search II.py'
if __name__ == "__main__":
  s = Solution()

  # Test Cases
  t1 = s.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"])
  t2 = s.findWords([["a","b"],["c","d"]], ["abcb"])

  # Output
  print(t1)
  print(t2)

  # Expected
  assert t1 == ["oath","eat"]
  assert t2 == []
