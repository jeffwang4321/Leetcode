from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ## Method 1
        # counts = {}
        # freq = [[] for i in range(len(nums) + 1)] # +1 bc max count is 6, so we want to get 0-6 rows
        # # print(freq) # [[], [], [], [], [], [], []]

        # for num in nums:
        #     counts[num] = 1 + counts.get(num, 0)
        # # print(counts) # {1: 3, 2: 2, 3: 1}

        # for num, count in counts.items():
        #     # print(num, count)   # 1 3, 2 2, 3 1
        #     freq[count].append(num)
        # # print(freq)   # [[], [3], [2], [1], [], [], []]
        # # Array freq[counts] maps to a list of nums that have that 'count' occurence
        # # i.e: 1 occurs 3 times, so its stored in freq[3]

        # res = []
        # for i in range(len(freq) - 1, 0, -1):
        #     for n in freq[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             return res

        ## Method 2: Hash Map and Sorting (Manual Frequency Count)
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        # print(count) # {1: 3, 2: 2, 3: 1}

        # print(count.values()) # [3, 2, 1]
        sorted_frequencies = sorted(count.values())
        # print(sorted_frequencies) # [1, 2, 3]
        threshold = sorted_frequencies[-k]  # 2

        res = []
        for num, freq in count.items():
            if freq >= threshold:
                res.append(num)
        return res


# python3 '.\297. Serialize and Deserialize Binary Tree.py'
if __name__ == "__main__":
    s = Solution()

    # Test Cases
    t1 = s.topKFrequent([1, 1, 1, 2, 2, 3], 2)
    t2 = s.topKFrequent([1], 1)

    # Output
    print(t1)  # [1, 2]
    print(t2)  # [1]
