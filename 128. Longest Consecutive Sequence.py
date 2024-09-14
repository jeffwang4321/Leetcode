from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ## Method 1: Hash Set Approach
        # num_set = set(nums)
        # max_length = 0

        # for num in num_set:
        #     if num - 1 not in num_set:
        #         current_length = 1
        #         while num + current_length in num_set:
        #             current_length += 1
        #         max_length = max(max_length, current_length)
        # return max_length

        ## Method 2: Sorting Approach
        if not nums:
            return 0

        nums = list(set(nums))
        nums.sort()

        max_length = 1
        current_length = 1

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                current_length += 1
            else:
                current_length = 1
            max_length = max(max_length, current_length)
        return max_length


if __name__ == "__main__":
    s = Solution()

    # Test Cases
    t1 = s.longestConsecutive([100, 4, 200, 1, 3, 2])
    t2 = s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])

    # Output
    print(t1)
    print(t2)
