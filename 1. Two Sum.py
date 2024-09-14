from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force Approach - Nested list/loop
        # Time complexity O(n^2), Space complexity O(1)
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # Optimal Approach - Hashmap
        # Time complexity O(n), Space complexity O(n)
        # hashmap = {value : index} -> hashmap[value] = index
        searched = {}
        for i in range(len(nums)):
            # 7 = 9 - 2 (nums[0])
            difference = target - nums[i]

            # If found
            if difference in searched:
                # return [index of 2, index of 7]
                return [i, searched[difference]]
            # Not found
            # searched[2] = 0
            searched[nums[i]] = i


# python3 '.\1. Two Sum.py'
if __name__ == "__main__":
    s = Solution()

    # Test Cases
    t1 = sorted(s.twoSum([2, 7, 11, 15], 9))
    t2 = sorted(s.twoSum([3, 2, 4], 6))
    t3 = sorted(s.twoSum([3, 3], 6))

    # Output
    print(t1)
    print(t2)
    print(t3)

    # Expected
    assert t1 == [0, 1]
    assert t2 == [1, 2]
    assert t3 == [0, 1]
