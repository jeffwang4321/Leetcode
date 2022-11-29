from typing import List

class Solution:
  def search(self, nums: List[int], target: int) -> int:
    # BRUTE FORCE
    # Time: O(n) - 1 loop, Space: O(1)
    # for i, num in enumerate(nums):
    #   if num == target:
    #     return i
    
    # return -1

    # OPTIMAL
    # Time: O(log n) - Binary Search, Space: O(1)
    l = 0
    r = len(nums) - 1

    while l <= r:
      mid = (l + r) // 2
      if target == nums[mid]:
        return mid

      # left sorted portion
      if nums[l] <= nums[mid]:
        if target > nums[mid] or target < nums[l]:
          l = mid + 1
        else:
          r = mid - 1

      # right sorted portion
      else:
        if target < nums[mid] or target > nums[r]:
          r = mid - 1
        else:
          l = mid + 1

    return -1



# python3 '.\33. Search in Rotated Sorted Array.py'
if __name__ == "__main__":
  s = Solution()

  # Test Cases
  t1 = s.search([4,5,6,7,0,1,2], 0)
  t2 = s.search([4,5,6,7,0,1,2], 3)
  t3 = s.search([1], 0)

  # Output
  print(t1)
  print(t2)
  print(t3)

  # Expected
  assert t1 == 4
  assert t2 == -1
  assert t3 == -1
