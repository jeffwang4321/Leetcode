class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Brute force - using str
        # Time: O(n), Space O(n)
        string = str(x)
        total = len(string)
        half = total // 2

        for i in range(half):
            if string[i] != string[-1 - i]:
                return False

        return True

        # if x < 0: return False

        # div = 1
        # while x > 10 * div:
        #     div *= 10

        # while x:
        #     right = x % 10
        #     left = x // div

        #     if left != right: return False

        #     x = (x % div) // 10 # chop left and right off x
        #     div = div / 100

        # return True


# python3 '.\9. Palindrome Number.py'
if __name__ == "__main__":
    s = Solution()

    # Test Cases
    t1 = s.isPalindrome("121")
    t2 = s.isPalindrome("-121")
    t3 = s.isPalindrome("10")

    # Output
    print(t1)
    print(t2)
    print(t3)

    # Expected
    assert t1 == True
    assert t2 == False
    assert t3 == False
