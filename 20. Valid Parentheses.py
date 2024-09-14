from typing import List


class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        char_map = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in char_map.values():
                stack.append(char)  # append opening brackets
            elif char in char_map:
                top_char = stack.pop() if stack else "#"
                if char_map[char] != top_char:
                    return False
        # if len(stack):
        #     return False
        # else:
        #     return True

        # return False if stack else True
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
