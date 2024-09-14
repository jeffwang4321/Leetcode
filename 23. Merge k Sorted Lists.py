from typing import Optional, List


# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))

            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next


def list_to_linkedlist(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linkedlist_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    s = Solution()

    # Test Case 1
    lists1 = [list_to_linkedlist([1, 4, 5]), list_to_linkedlist([1, 3, 4]), list_to_linkedlist([2, 6])]
    result1 = s.mergeKLists(lists1)
    print(linkedlist_to_list(result1))  # Expected output: [1, 1, 2, 3, 4, 4, 5, 6]

    # Test Case 2
    lists2 = [list_to_linkedlist([]), list_to_linkedlist([]), list_to_linkedlist([])]
    result2 = s.mergeKLists(lists2)
    print(linkedlist_to_list(result2))  # Expected output: []

    # Test Case 3
    lists3 = [list_to_linkedlist([1]), list_to_linkedlist([0])]
    result3 = s.mergeKLists(lists3)
    print(linkedlist_to_list(result3))  # Expected output: [0, 1]
