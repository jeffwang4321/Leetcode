from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # # Method 1:
        # return min(nums)

        # Optimal:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]


if __name__ == "__main__":
    s = Solution()

    # Test Cases
    t1 = s.findMin([3, 4, 5, 1, 2])
    t2 = s.findMin([4, 5, 6, 7, 0, 1, 2])
    t3 = s.findMin([11, 13, 15, 17])

    # Output
    print(t1)
    print(t2)
    print(t3)
