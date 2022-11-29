from typing import List

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    # Time: O(n), Space: O(1)
    # l = 0
    # res = 0
    # for r in range(1, len(prices)):
    #   if prices[r] < prices[l]:
    #     l = r
    #   res = max(res, prices[r] - prices[l])
    
    # return res

    res = 0
    l = 0
    for r in range(1, len(prices)):
      if prices[r] > prices[l]:
        res = max(res, prices[r] - prices[l])
      if prices[r] < prices[l]:
        l = r

    return res



# python3 '.\121. Best Time to Buy and Sell Stock.py'
if __name__ == "__main__":
  s = Solution()

  # Test Cases
  t1 = s.maxProfit([7,1,5,3,6,4])
  t2 = s.maxProfit([7,6,4,3,1])

  # Output
  print(t1)
  print(t2)

  # Expected
  assert t1 == 5
  assert t2 == 0
