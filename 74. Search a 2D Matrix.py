class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        ## Brute Force - Nested Loop
        # Time: O(n^2)
        # for row in matrix:
        #     for num in row:
        #         if num == target:
        #             return True
        # return False

        ## Optimal - Nested loops using binary search
        ## Time: O(log(m * n))
        ## 2D Binary Search
        if not matrix or not matrix[0]:
            return False

        ROWS, COLS = len(matrix), len(matrix[0])

        # Binary search for the correct row
        top_row, bot_row = 0, ROWS - 1

        while top_row <= bot_row:
            mid_row = (top_row + bot_row) // 2
            if target > matrix[mid_row][-1]:
                top_row = mid_row + 1
            elif target < matrix[mid_row][0]:
                bot_row = mid_row - 1
            else:
                break
        else:
            return False  # Target is not within the range of any row

        # Binary search within the row
        left, right = 0, COLS - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid_row][mid] == target:
                return True
            elif matrix[mid_row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


# Example Usage
if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    print(sol.searchMatrix(matrix, 3))  # Output: True

    print(sol.searchMatrix(matrix, 13))  # Output: False
