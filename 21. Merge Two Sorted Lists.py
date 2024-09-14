from typing import Optional, List


# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        return dummy.next


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

    # Test Case 1
    test_list1a = [1, 2, 4]
    test_list1b = [1, 3, 4]
    head1a = list_to_linkedlist(test_list1a)
    head1b = list_to_linkedlist(test_list1b)
    s1 = s.mergeTwoLists(head1a, head1b)
    print(linkedlist_to_list(s1))  # Expected: [1, 1, 2, 3, 4, 4]

    # Test Case 2
    test_list2a = []
    test_list2b = []
    head2a = list_to_linkedlist(test_list2a)
    head2b = list_to_linkedlist(test_list2b)
    s2 = s.mergeTwoLists(head2a, head2b)
    print(linkedlist_to_list(s2))  # Expected: []

    # Test Case 3
    test_list3a = []
    test_list3b = [0]
    head3a = list_to_linkedlist(test_list3a)
    head3b = list_to_linkedlist(test_list3b)
    s3 = s.mergeTwoLists(head3a, head3b)
    print(linkedlist_to_list(s3))  # Expected: [0]
