import heapq
import bisect


class MedianFinder:

    def __init__(self):
        # # # Approach 1 - Brute Force - Sorted list
        # # List to store the stream of numbers in sorted order
        # self.nums = []

        # # Approach 2 - Min Max heap
        # Max-heap for the lower half of the numbers
        self.low = []  # max-heap (inverted values)
        # Min-heap for the upper half of the numbers
        self.high = []  # min-heap

    def addNum(self, num: int) -> None:
        # # Approach 1 - Brute Force - Sorted list
        # bisect.insort(self.nums, num)

        # # Approach 2 - Min Max heap
        # Add to max-heap (inverted to simulate max behavior)
        heapq.heappush(self.low, -num)

        # Ensure every element in low is less than or equal to every element in high
        if self.low and self.high and (-self.low[0] > self.high[0]):
            # Move the root of max-heap (largest in low) to min-heap
            heapq.heappush(self.high, -heapq.heappop(self.low))

        # Balance the sizes of the two heaps
        if len(self.low) > len(self.high) + 1:
            # Move the root of max-heap (largest in low) to min-heap
            heapq.heappush(self.high, -heapq.heappop(self.low))
        elif len(self.high) > len(self.low):
            # Move the root of min-heap (smallest in high) to max-heap
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self) -> float:
        # # Approach 1 - Brute Force - Sorted list
        # n = len(self.nums)

        # if n % 2 == 1:
        #     return float(self.nums[n // 2])
        # else:
        #     return (self.nums[n // 2 - 1] + self.nums[n // 2]) / 2

        # # # Approach 2 - Min Max heap
        if len(self.low) > len(self.high):
            # If max-heap has more elements, return its root
            return -self.low[0]
        else:
            # If both heaps have the same size, return the average of the roots
            return (-self.low[0] + self.high[0]) / 2


# Example Usage
if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    print(mf.findMedian())  # Output: 1.5
    mf.addNum(3)
    print(mf.findMedian())  # Output: 2
