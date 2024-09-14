from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ## Brute Force - O(n^2)
        # n = len(nums)
        # output = [1] * n

        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i != j:
        #             output[i] *= nums[j]

        # return output

        ## Optimal: O(n)
        ## Prefix and suffix
        n = len(nums)
        output = [1] * n

        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output


# python3 '.\297. Serialize and Deserialize Binary Tree.py'
if __name__ == "__main__":
    s = Solution()

    # Test Cases
    t1 = s.productExceptSelf([1, 2, 3, 4])
    t2 = s.productExceptSelf([-1, 1, 0, -3, 3])

    # Output
    print(t1)
    print(t2)
