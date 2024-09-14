class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Approach 1: Filter str and compare with reversed string
        # filtered = []
        # for c in s:
        #     if c.isalnum():
        #         filtered.append(c.lower())
        # filtered = "".join(filtered)
        # filtered = "".join(char.lower() for char in s if char.isalnum())
        # return filtered == filtered[::-1]

        # # Approach 2: 2 Pointer
        l = 0
        r = len(s) - 1

        while l < r:
            while not s[l].isalnum() and l < r:
                l += 1
            while not s[r].isalnum() and l < r:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


if __name__ == "__main__":
    s = Solution()

    # Test Cases
    t1 = s.isPalindrome("A man, a plan, a canal: Panama")
    t2 = s.isPalindrome("race a car")
    t3 = s.isPalindrome(" ")

    # Output
    print(t1)
    print(t2)
    print(t3)
