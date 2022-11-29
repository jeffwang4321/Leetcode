from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Time: O(n * m * dfs) where n * m is the board dimensions and dfs = O(4^len(word)) = O(4^w)
        ROWS = len(board)
        COLS = len(board[0])
        path = set()

        def dfs(r, c, i): # row, col, index = current char
            if i == len(word):
                return True

            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return False 

            if word[i] != board[r][c] or (r, c) in path:
                return False
            
            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                    dfs(r - 1, c, i + 1) or
                    dfs(r, c + 1, i + 1) or
                    dfs(r, c - 1, i + 1))
            
            path.remove((r,c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        
        return False



# python3 '.\79. Word Search.py'
if __name__ == "__main__":
  s = Solution()

  # Test Cases
  t1 = s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
  t2 = s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")
  t3 = s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCD")

  # Output
  print(t1)
  print(t2)
  print(t3)

  # Expected
  assert t1 == True
  assert t2 == True
  assert t3 == False
