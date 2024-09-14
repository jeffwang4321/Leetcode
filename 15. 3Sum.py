from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # # BRUTE FORCE - O(n^3) - Nested list/ for loop
        # # Time complexity O(n^3), Space complexity O(n)
        # res = []
        # for i in range(len(nums) - 2):
        #     for j in range(i + 1, len(nums) - 1):
        #         for k in range(j + 1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 triplet = sorted([nums[i], nums[j], nums[k]])
        #                 if triplet not in res:
        #                     res.append(triplet)
        # return res

        # # OPTIMAL
        # # Method - sort input arr so that we can check for duplicate on previous input
        # # Optimized using Two Pointer technique
        # # Time complexity O(n^2), Space complexity O(1)
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]

                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # Check and skip duplicated
                    # while l < r and nums[l] == nums[l + 1]:
                    #     l += 1
                    # while l < r and nums[r] == nums[r - 1]:
                    # r -= 1
                    l += 1
                    r -= 1
                    # r -= 1

        return res


# python3 '.\15. 3Sum.py'
if __name__ == "__main__":
    s = Solution()

    # Test Cases
    t1 = s.threeSum([-1, 0, 1, 2, -1, -4])
    t2 = s.threeSum([0, 1, 1])
    t3 = s.threeSum([0, 0, 0])

    # Output
    print(t1)
    print(t2)
    print(t3)
