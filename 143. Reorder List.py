from typing import Optional, List


# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Get middle of the list - using turtle and hare algo, slow.next is middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split and reverse the second half of the list
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Merge the 2 halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


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

    # Test Case 1: Even number of elements
    test_list2 = [1, 2, 3, 4]
    head2 = list_to_linkedlist(test_list2)
    s.reorderList(head2)
    print(linkedlist_to_list(head2))  # Expected output: [1, 4, 2, 3]

    # Test Case 2: Odd number of elements
    test_list1 = [1, 2, 3, 4, 5]
    head1 = list_to_linkedlist(test_list1)
    s.reorderList(head1)
    print(linkedlist_to_list(head1))  # Expected output: [1, 5, 2, 4, 3]

    # Test Case 3: Single element
    test_list3 = [1]
    head3 = list_to_linkedlist(test_list3)
    s.reorderList(head3)
    print(linkedlist_to_list(head3))  # Expected output: [1]

    # Test Case 4: Two elements
    test_list4 = [1, 2]
    head4 = list_to_linkedlist(test_list4)
    s.reorderList(head4)
    print(linkedlist_to_list(head4))  # Expected output: [1, 2]

    # Test Case 5: Empty list
    test_list5 = []
    head5 = list_to_linkedlist(test_list5)
    s.reorderList(head5)
    print(linkedlist_to_list(head5))  # Expected output: []
