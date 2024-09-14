from typing import List


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        res = 0

        for r, char in enumerate(s):
            count[char] = 1 + count.get(char, 0)

            # Note window size is (r - l + 1)
            if (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res


if __name__ == "__main__":
    sol = Solution()

    # Test Cases
    s = "ABAB"
    k = 2
    t1 = sol.characterReplacement(s, k)
    s = "AABABBA"
    k = 1
    t2 = sol.characterReplacement(s, k)

    # Output
    print(t1)
    print(t2)
