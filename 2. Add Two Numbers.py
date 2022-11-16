from typing import Optional

# Definition for singly-linked list
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      
    dummy = ListNode()
    current = dummy
    
    carry = 0
    while l1 or l2 or carry:
      v1 = l1.val if l1 else 0
      v2 = l2.val if l2 else 0
      
      # new digit
      val = v1 + v2 + carry
      
      carry = val // 10
      val = val % 10
      
      current.next = ListNode(val)
      
      # Update Ptrs
      current = current.next
      l1 = l1.next if l1 else None
      l2 = l2.next if l2 else None
        
    return dummy.next



# python3 '.\2. Add Two Numbers.py'
if __name__ == "__main__":
  s = Solution()

  c = ListNode(3)
  b = ListNode(4, c)
  a = ListNode(2, b)

  x = ListNode(4)
  y = ListNode(6, x)
  z = ListNode(5, y)


  # Test Cases
  t1 = s.addTwoNumbers(l1 = a, l2 = z)

  # Output
  l = []
  while t1 is not None:
    l.append(t1.val)
    t1 = t1.next  

  print(l)

  # Expected
  assert l == [7,0,8]

