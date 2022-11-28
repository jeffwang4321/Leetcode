from typing import List

class Solution:
  def maxArea(self, height: List[int]) -> int:
    # BRUTE FORCE  
    # Time: O(n^2)

    # res = 0
    
    # for l in range(len(height)):
    #   for r in range(l + 1, len(height)):
    #     area = (r - l) * min(height[l], height[r])
    #     res = max(res, area)
    
    # return res

    res = 0
    l, r = 0, len(height) - 1
    
    while l < r:
      area = (r - l) * min(height[l], height[r])
      res = max(res, area)
      
      if height[l] < height[r]:
        l += 1
      else:
        r -= 1
    
    return res


# python3 '.\11. Container With Most Water.py'
if __name__ == "__main__":
  s = Solution()

  # Test Cases
  t1 = s.maxArea([1,8,6,2,5,4,8,3,7])
  t2 = s.maxArea([1,1])

  # Output
  print(t1)
  print(t2)

  # Expected
  assert t1 == 49
  assert t2 == 1
