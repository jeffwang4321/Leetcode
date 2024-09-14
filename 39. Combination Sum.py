class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def backtrack(start, target, path):
            if target == 0:
                result.append(path)
                return

            if target < 0:
                return

            for i in range(start, len(candidates)):
                # dont use path.append(candidates[i])
                backtrack(i, target - candidates[i], path + [candidates[i]])
                # or we have to path.pop() after the backtrack()

        result = []
        backtrack(0, target, [])
        return result


# Example Usage
if __name__ == "__main__":
    sol = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    print(sol.combinationSum(candidates, target))
    # Output: [[2, 2, 3], [7]]

    candidates = [2, 3, 5]
    target = 8
    print(sol.combinationSum(candidates, target))
    # Output: [[2,2,2,2],[2,3,3],[3,5]]

    candidates = [2]
    target = 1
    print(sol.combinationSum(candidates, target))
    # Output: []
