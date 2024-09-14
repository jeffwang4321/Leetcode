from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Brute Force:
        # if not s or not t:
        #     return ""

        # t_freq = Counter(t)
        # min_len = float("inf")
        # min_window = ""
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         current_substring = s[i : j + 1]
        #         window_freq = Counter(current_substring)

        #         valid = True
        #         for char in t_freq:
        #             if window_freq[char] < t_freq[char]:
        #                 valid = False
        #                 break

        #         if valid:
        #             if (j - i + 1) < min_len:
        #                 min_len = j - i + 1
        #                 min_window = current_substring

        # return min_window

        # Optimal
        if not s or not t:
            return ""

        t_freq = Counter(t)
        window_freq = {}
        have, need = 0, len(t_freq)
        min_len = float("inf")
        res_left, res_right = 0, 0

        left = 0

        for right in range(len(s)):
            char = s[right]
            window_freq[char] = window_freq.get(char, 0) + 1

            if char in t_freq and window_freq[char] == t_freq[char]:
                have += 1

            while have == need:
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    res_left, res_right = left, right

                char = s[left]
                window_freq[char] -= 1
                if char in t_freq and window_freq[char] < t_freq[char]:
                    have -= 1
                left += 1

        return s[res_left : res_right + 1] if min_len != float("inf") else ""


# python3 '.\1. Two Sum.py'
if __name__ == "__main__":
    sol = Solution()

    # Test Cases
    t1 = sol.minWindow(s="ADOBECODEBANC", t="ABC")
    t2 = sol.minWindow(s="a", t="a")
    t3 = sol.minWindow(s="a", t="aa")

    # Output
    print(t1)
    print(t2)
    print(t3)
