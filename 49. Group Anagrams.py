from typing import List
from collections import defaultdict, Counter


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Method 1: Sorting-Based Approach
        # Time: O(n * k log k), n is the number of strings and k is the max length of a string (sorting each string)
        # Space: O(n * k) for storing the results

        hashmap = defaultdict(list)

        for s in strs:
            ### keys can be strings or tuple, bc they are immutable
            # key = str(Counter(s).items())
            # key = tuple(sorted(s)) # tuple is a hashable, fixed collection of items e.g (1, "a", 2.0)

            key = "".join(sorted(s))  # 'abc' vs below ['a', 'b', 'c']
            # key = str(sorted(s))  # ['a', 'b', 'c']

            hashmap[key].append(s)
        return list(hashmap.values())


# python3 '.\33. Search in Rotated Sorted Array.py'
if __name__ == "__main__":
    s = Solution()

    # Test Cases
    t1 = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    t2 = s.groupAnagrams([""])
    t3 = s.groupAnagrams(["a"])

    # Output
    print(t1)
    print(t2)
    print(t3)
