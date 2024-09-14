from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # # # Method 1: Recursion
        # if p is None and q is None:
        #     return True
        # elif p is None or q is None:
        #     return False
        # elif p.val != q.val:
        #     return False

        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # # Method 2: stack
        stack = [(p, q)]

        while stack:
            node1, node2 = stack.pop()

            if node1 is None and node2 is None:
                continue
            elif node1 is None or node2 is None:
                return False
            elif node1.val != node2.val:
                return False

            stack.append((node1.left, node2.left))
            stack.append((node1.right, node2.right))

        return True


def print_tree(root):
    if not root:
        print("None")
        return

    queue = deque([root])
    result = []

    while queue:
        current = queue.popleft()
        if current:
            result.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append(None)

    # To avoid trailing None values which are not meaningful in visualizing the tree structure
    while result and result[-1] is None:
        result.pop()

    print(result)


# python3 '.\104. Maximum Depth of Binary Tree.py'
if __name__ == "__main__":
    # Creating the example trees
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)

    # Print the original trees
    print("Tree p:")
    print_tree(p)
    print("Tree q:")
    print_tree(q)

    # Solution instance
    solution = Solution()

    # Test if the trees are the same
    print("Are the trees the same?", solution.isSameTree(p, q))  # Output: True

    # Additional test case 1 (different structures)
    print("\nTest Case 1:")
    # Tree p: 1 -> (2, None)
    # Tree q: 1 -> (None, 2)
    p1 = TreeNode(1)
    p1.left = TreeNode(2)

    q1 = TreeNode(1)
    q1.right = TreeNode(2)

    print("Tree p1:")
    print_tree(p1)
    print("Tree q1:")
    print_tree(q1)
    print("Are the trees the same?", solution.isSameTree(p1, q1))  # Output: False

    # Additional test case 2 (empty trees)
    print("\nTest Case 2:")
    p2 = None
    q2 = None
    print("Tree p2:", end=" ")
    print_tree(p2)
    print("Tree q2:", end=" ")
    print_tree(q2)
    print("Are the trees the same?", solution.isSameTree(p2, q2))  # Output: True
