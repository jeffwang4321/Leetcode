from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Time: O(n * m * dfs) where n * m is the board dimensions and dfs = O(4^len(word)) = O(4^w)
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()

        def dfs(row, col, index):  # row, col, index = current char
            if index == len(word):
                return True

            if row < 0 or col < 0 or row >= ROWS or col >= COLS:
                return False

            if word[index] != board[row][col] or (row, col) in visited:
                return False

            visited.add((row, col))
            found = (
                dfs(row + 1, col, index + 1)
                or dfs(row - 1, col, index + 1)
                or dfs(row, col + 1, index + 1)
                or dfs(row, col - 1, index + 1)
            )

            visited.remove((row, col))
            return found

        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0):
                    return True

        return False


# python3 '.\79. Word Search.py'
if __name__ == "__main__":
    s = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    # Test Cases
    t1 = s.exist(board, "ABCCED")
    t2 = s.exist(board, "SEE")
    t3 = s.exist(board, "ABCD")

    # Output
    print(t1)
    print(t2)
    print(t3)

    # Expected
    assert t1 == True
    assert t2 == True
    assert t3 == False
