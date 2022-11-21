from typing import List

class Solution:
  # when int in list a + int in list b = target, hit++
  def twoSum(self, a: List[int], b: List[int], target: int) -> List[int]:
    # arr = []

    # for i in a:
    #   hit = 0
    #   for j in b:
    #     if i + j == target:
    #       hit += 1
    #   arr.append(hit)
    # return arr

    arr = []
    differences = []
    for i in b:
      diff = target - i
      differences.append(diff)
    
    for j in a:
      arr.append(differences.count(j))

    return arr

    


# python3 '.\0. TestRBC.py'
if __name__ == "__main__":
  s = Solution()

  # Test Cases
  t1 = s.twoSum([2,7,2,11,15], [2,7,11,15,7,7], 9)
  t2 = s.twoSum([3,2,4], [3,2,4], 6)
  t3 = s.twoSum([3,3], [3,3], 6)

  # Output
  print(t1)
  print(t2)
  print(t3)

  # Expected
  # assert t1 == [3, 1, 0, 0]
  # assert t2 == [1, 1, 1]
  # assert t3 == [2, 2]
  
