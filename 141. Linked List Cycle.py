from typing import Optional, List


# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # # # Brute force - visited set
        # visited = set()
        # current = head

        # while current:
        #     if current in visited:
        #         return True
        #     visited.add(current)
        #     current = current.next

        # return False

        # # Optimal: turtle and hare algo
        if not head:
            return False

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False


def list_to_linkedlist(lst: List[int], cycle_pos: int) -> Optional[ListNode]:
    if not lst:
        return None

    head = ListNode(lst[0])
    current = head
    nodes = [head]
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
        nodes.append(current)

    # Create cycle if cycle_pos is valid
    if cycle_pos != -1:
        current.next = nodes[cycle_pos]

    return head


def linkedlist_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    s = Solution()

    # Test Case 1: List with a cycle
    head1 = list_to_linkedlist(lst=[3, 2, 0, -4], cycle_pos=1)
    print(s.hasCycle(head1))  # Expected: True

    # Test Case 2: List with a cycle
    head2 = list_to_linkedlist(lst=[1, 2], cycle_pos=0)
    print(s.hasCycle(head2))  # Expected: True

    # Test Case 3: List without a cycle
    head3 = list_to_linkedlist(lst=[1], cycle_pos=-1)
    print(s.hasCycle(head3))  # Expected: False
