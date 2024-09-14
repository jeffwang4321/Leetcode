from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Slightly more efficient due to only sorting half the total length
        # Time: O(log(n)), Space: O(n) - list/array
        totalLen = len(nums1) + len(nums2)
        half = totalLen // 2
        i = 0
        array = []

        while i <= half:
            if len(nums1) and len(nums2):
                if nums1[0] < nums2[0]:
                    array.append(nums1[0])  # append to the end of the list
                    nums1.pop(
                        0
                    )  # remove elem from list[0], can get/store/print this value
                else:
                    array.append(nums2[0])
                    nums2.pop(0)
            elif len(nums1):
                array.append(nums1[0])
                nums1.pop(0)
            elif len(nums2):
                array.append(nums2[0])
                nums2.pop(0)
            i += 1

        # odd
        if totalLen % 2:
            return array[-1]
        # even
        else:
            return (array[-1] + array[-2]) / 2

        # Time: O(nlogn) - timsort, Space: O(n) - list/ timsort
        # total = sorted(nums1 + nums2) # sorted() is O(nlogn)
        # half = len(total) // 2

        # # odd
        # if len(total) % 2:
        #   return total[half]
        # # even
        # else:
        #   return (total[half] + total[half-1]) / 2


# python3 '.\4. Median of Two Sorted Arrays.py'
if __name__ == "__main__":
    s = Solution()

    # Test Cases
    t1 = s.findMedianSortedArrays([1, 3], [2])
    t2 = s.findMedianSortedArrays([1, 2], [3, 4])

    # Output
    print(t1)
    print(t2)

    # Expected
    assert t1 == 2
    assert t2 == 2.5
