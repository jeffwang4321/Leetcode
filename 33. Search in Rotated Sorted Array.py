from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        # # Method 1:
        # return nums.index(target) if target in nums else -1

        # # BRUTE FORCE
        # # Time: O(n) - 1 loop, Space: O(1)
        # for i, num in enumerate(nums):
        #   if num == target:
        #     return i
        # return -1

        # # OPTIMAL
        # # Time: O(log n) - Binary Search, Space: O(1)
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]:  # left half is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # right half is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


# python3 '.\33. Search in Rotated Sorted Array.py'
if __name__ == "__main__":
    s = Solution()

    # Test Cases
    t1 = s.search([4, 5, 6, 7, 0, 1, 2], 0)
    t2 = s.search([4, 5, 6, 7, 0, 1, 2], 3)
    t3 = s.search([1], 0)

    # Output
    print(t1)
    print(t2)
    print(t3)

    # Expected
    assert t1 == 4
    assert t2 == -1
    assert t3 == -1
