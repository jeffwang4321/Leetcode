from typing import List

class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    # BRUTE FORCE
    # Time: O(nlogn) - 1 sort, Space: O(1)
    # nums.sort() # nums = sorted(nums)
    # for i in range(1, len(nums)):
    #   if nums[i] == nums[i-1]:
    #     return True
    
    # return False

    # OPTIMAL
    # Time: O(n) - 1 set, Space: O(n)
    # return len(nums) != len(set(nums))

    # OPTIMAL
    # Time: O(n) - 1 loop, Space: O(n)
    # Method - insert into set() check if num already exists 
    # hashMap = set()
    # for i in nums:
    #   if i in hashMap:
    #     return True
    #   else:
    #     hashMap.add(i)
        
    # return False

    


# python3 '.\217. Contains Duplicate.py'
if __name__ == "__main__":
  s = Solution()

  # Test Cases
  t1 = s.containsDuplicate([1,2,3,1])
  t2 = s.containsDuplicate([1,2,3,4])
  t3 = s.containsDuplicate([1,1,1,3,3,4,3,2,4,2])

  # Output
  print(t1)
  print(t2)
  print(t3)

  # Expected
  assert t1 == True
  assert t2 == False
  assert t3 == True
