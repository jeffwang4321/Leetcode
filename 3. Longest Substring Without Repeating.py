class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    # Time: O(n) - loop, Space: O(n) - 1 set
    charSet = set()
    l = 0
    res = 0
    
    for r in range(len(s)):
      while s[r] in charSet:
        charSet.remove(s[l]) # Remove elem from list/set
        l += 1
      charSet.add(s[r]) # Add  elem to set
      # res = max(res, r - l + 1) -> r - l + 1 = length of [arr[l]... arr[r]] = len(arr[l:r+1]) 
      res = max(res, len(charSet)) 
        
    return res



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