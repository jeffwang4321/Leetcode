class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # # Approach 1: storing substring

        substring = ""
        longest = 0
        for c in s:
            while c in substring:
                substring = substring[1:]
            substring += c
            longest = max(longest, len(substring))

        return longest

        # # Time: O(n) - loop, Space: O(n) - 1 set
        # substring = set()
        # longest = 0
        # left = 0

        # for right, char in enumerate(s):
        #     while char in substring:
        #         substring.remove(s[left])
        #         left += 1
        #     substring.add(char)
        #     longest = max(longest, len(substring))

        # return longest


# python3 '.\1. Two Sum.py'
if __name__ == "__main__":
    s = Solution()

    # Test Cases
    t1 = s.lengthOfLongestSubstring("abcabcbb")
    t2 = s.lengthOfLongestSubstring("bbbbb")
    t3 = s.lengthOfLongestSubstring("pwwkew")

    # Output
    print(t1)
    print(t2)
    print(t3)

    # Expected
    assert t1 == 3
    assert t2 == 1
    assert t3 == 3
