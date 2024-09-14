from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # # BRUTE FORCE
        # # Time: O(n^2) - 2 loops, Space: O(1) - ints
        # max_area = 0
        # for left in range(len(height)):
        #     for right in range(left + 1, len(height)):
        #         area = (right - left) * min(height[left], height[right])
        #         max_area = max(max_area, area)

        # return max_area

        # # OPTIMAL
        # # Time: O(n) - 1 loop, Space: O(1) - ints
        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


# python3 '.\11. Container With Most Water.py'
if __name__ == "__main__":
    s = Solution()

    # Test Cases
    t1 = s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    t2 = s.maxArea([1, 1])

    # Output
    print(t1)
    print(t2)

    # Expected
    assert t1 == 49
    assert t2 == 1
