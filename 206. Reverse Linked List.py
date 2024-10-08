from typing import Optional, List


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
            next_node = curr.next  # Save the next node
            curr.next = prev  # Reverse the link
            prev = curr  # Move prev to current node
            curr = next_node  # Move to the next node

        return prev


def list_to_linkedlist(lst: List[int]) -> Optional[ListNode]:
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linkedlist_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# python3 '.\206. Reverse Linked List.py'
if __name__ == "__main__":
    s = Solution()

    test_list1 = [1, 2, 3, 4, 5]
    head1 = list_to_linkedlist(test_list1)
    reversed_head1 = s.reverseList(head1)
    print(linkedlist_to_list(reversed_head1))

    test_list2 = [1, 2]
    head2 = list_to_linkedlist(test_list2)
    reversed_head2 = s.reverseList(head2)
    print(linkedlist_to_list(reversed_head2))

    test_list3 = []
    head3 = list_to_linkedlist(test_list3)
    reversed_head3 = s.reverseList(head3)
    print(linkedlist_to_list(reversed_head3))
