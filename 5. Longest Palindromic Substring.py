class Solution:
    # def longestPalindrome(self, s: str) -> str:
    #     # Expand Around the Center - Time: O(n^2)
    #     bestLen = 0
    #     start, end = 0, 0
        
    #     for i in range(len(s)):
            
    #         # odd length
    #         l, r = i, i
    #         while l >= 0 and r < len(s) and s[l] == s[r]:
    #             if(r - l + 1) > bestLen:
    #                 # res = s[l:r + 1]
    #                 start = l
    #                 end = r + 1
    #                 bestLen = r - l + 1
    #             l -= 1
    #             r += 1
            
    #         # even length
    #         l, r = i, i + 1
    #         while l >= 0 and r < len(s) and s[l] == s[r]:
    #             if(r - l + 1) > bestLen:
    #                 # res = s[l:r + 1]
    #                 start = l
    #                 end = r + 1
    #                 bestLen = r - l + 1
    #             l -= 1
    #             r += 1
        
    #     return s[start:end]

    # Expand Around the i/Center - Time: O(n^2)
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):        
            odd  = self.palindromeAt(s, i, i)
            even = self.palindromeAt(s, i, i+1)
            
            res = max(res, odd, even, key=len)
        return res
 
    # starting at l,r expand outwards to find the biggest palindrome
    def palindromeAt(self, s: str, l: int, r: int) -> str:    
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]



# python3 '.\5. Longest Palindromic Substring.py'
if __name__ == "__main__":
  s = Solution()

  # Test Cases
  t1 = s.longestPalindrome("babad")
  t2 = s.longestPalindrome("cbbd")

  # Output
  print(t1)
  print(t2)

  # Expected
  assert t1 == "bab"
  assert t2 == "bb"
