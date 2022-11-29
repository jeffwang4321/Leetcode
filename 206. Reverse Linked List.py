from typing import Optional

# Definition for singly-linked list
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head

    while curr:
      temp = curr.next
      curr.next = prev
      prev = curr
      curr = temp
    return prev



# python3 '.\206. Reverse Linked List.py'
if __name__ == "__main__":
  s = Solution()

  e = ListNode(5)
  d = ListNode(4, e)
  c = ListNode(3, d)
  b = ListNode(2, c)
  a = ListNode(1, b)

  # Test Cases
  t1 = s.reverseList(a)

  # Output
  l = []
  while t1 is not None:
    l.append(t1.val)
    t1 = t1.next  

  print(l)

  # Expected
  assert l == [5,4,3,2,1]

