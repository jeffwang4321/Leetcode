from typing import List

class Solution:
  def isValid(self, s: str) -> bool:
    stack = []

    closeToOpen = {
      ")" : "(",
      "]" : "[",
      "}" : "{"
    }

    for char in s:
      if char not in closeToOpen:
        stack.append(char) # append opening brackets 
      else:
        # if len(stack) > 0 and stack[len(stack)-1] == closeToOpen[char]:
        if stack and stack[-1] == closeToOpen[char]:
          stack.pop()
        else:
          return False
    
    # if len(stack):
    #     return False
    # else:
    #     return True
    return not stack
    


# python3 '.\20. Valid Parentheses.py'
if __name__ == "__main__":
  s = Solution()

  # Test Cases
  t1 = s.isValid("()")
  t2 = s.isValid("()[]{}")
  t3 = s.isValid("(]")

  # Output
  print(t1)
  print(t2)
  print(t3)

  # Expected
  assert t1 == True
  assert t2 == True
  assert t3 == False
