from typing import Optional, List


# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        position_remove = length - n

        if position_remove == 0:
            return head.next

        curr = head
        for _ in range(position_remove - 1):
            curr = curr.next

        curr.next = curr.next.next
        return head


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


if __name__ == "__main__":
    s = Solution()

    test_list2 = [1, 2, 3, 4, 5]
    head2 = list_to_linkedlist(test_list2)
    s.removeNthFromEnd(head2, n=2)
    print(linkedlist_to_list(head2))

    test_list1 = [1]
    head1 = list_to_linkedlist(test_list1)
    s.removeNthFromEnd(head1, n=1)
    print(linkedlist_to_list(head1))

    test_list3 = [1, 2]
    head3 = list_to_linkedlist(test_list3)
    s.removeNthFromEnd(head3, n=1)
    print(linkedlist_to_list(head3))
