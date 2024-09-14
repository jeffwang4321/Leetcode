from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # # Brute Force:
        # # Time: O(n^2)
        # max_profit = 0
        # for r in range(len(prices)):
        #     for l in range(r + 1, len(prices)):
        #         max_profit = max(max_profit, prices[l] - prices[r])

        # return max_profit

        # # Time: O(n), Space: O(1)
        # l = 0
        # res = 0
        # for r in range(1, len(prices)):
        #     if prices[r] < prices[l]:
        #         l = r
        #     else:
        #         res = max(res, prices[r] - prices[l])

        # return res

        # # Time: O(n), Space: O(1)
        if not prices:
            return 0

        max_profit = 0
        min_price = prices[0]  # Alt: min_price = float("inf")

        for price in prices[1:]:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit


# python3 '.\121. Best Time to Buy and Sell Stock.py'
if __name__ == "__main__":
    s = Solution()

    # Test Cases
    t1 = s.maxProfit([7, 1, 5, 3, 6, 4])
    t2 = s.maxProfit([7, 6, 4, 3, 1])

    # Output
    print(t1)
    print(t2)

    # Expected
    assert t1 == 5
    assert t2 == 0
