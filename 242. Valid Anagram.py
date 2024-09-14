class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Method 1 - Sort s and t, then compare
        # Time: O(nlogn), Space: O(1)
        # return sorted(s) == sorted(t)

        # Method 2 - Hashmap of counts, then compare counts
        # Time: O(n), Space: O(n) - 2 hashmaps
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        print(countS)
        print(countT)

        return countS == countT


# python3 '.\242. Valid Anagram.py'
if __name__ == "__main__":
    s = Solution()

    # Test Cases
    t1 = s.isAnagram("anagram", "nagaram")
    t2 = s.isAnagram("rat", "car")

    # Output
    print(t1)
    print(t2)

    # Expected
    assert t1 == True
    assert t2 == False
