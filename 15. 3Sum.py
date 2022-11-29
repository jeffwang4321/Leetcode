from typing import List

class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    # BRUTE FORCE - O(n^3) - Nested list/ for loop
    # Time complexity O(n^3), Space complexity O(1)
    # res = []
    # nums.sort() # sort input arr so that we can check for duplicate previous input
    
    # for i in range(len(nums)):
    #   if i > 0 and nums[i] == nums[i - 1]:
    #     continue
    #   for j in range(i + 1, len(nums)):
    #     if j > i + 1 and nums[j] == nums[j - 1]:
    #       continue
    #     for k in range(j + 1, len(nums)):
    #       if k > j + 1 and nums[k] == nums[k - 1]:
    #         continue
                  
    #       if nums[i] + nums[j] + nums[k] == 0:
    #         res.append([nums[i], nums[j], nums[k]])             
    # return res
      
    # OPTIMAL
    # Method - sort input arr so that we can check for duplicate on previous input 
    # Optimized using Two Pointer technique
    # Time complexity O(n^2), Space complexity O(1)
    res = []
    nums.sort()

    for i in range(len(nums)):
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
          l += 1

          # Check and skip duplicated
          while l < r and nums[l] == nums[l-1]:
            l += 1
            
    return res
    


# python3 '.\15. 3Sum.py'
if __name__ == "__main__":
  s = Solution()

  # Test Cases
  t1 = s.threeSum([-1,0,1,2,-1,-4])
  t2 = s.threeSum([0,1,1])
  t3 = s.threeSum([0,0,0])

  # Output
  print(t1)
  print(t2)
  print(t3)

  # Expected
  assert t1 == [[-1,-1,2],[-1,0,1]]
  assert t2 == []
  assert t3 == [[0,0,0]]
