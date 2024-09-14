from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # # Method 1: Recursive
        def isSameTree(s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
            if s is None and t is None:
                return True
            if s is None or t is None:
                return False
            if s.val != t.val:
                return False
            return isSameTree(s.left, t.left) and isSameTree(s.right, t.right)

        if root is None:
            return False

        if isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        # # Method 2: stack
        # def isSameTree(s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        #     stack = [(s, t)]
        #     while stack:
        #         node1, node2 = stack.pop()
        #         if node1 is None and node2 is None:
        #             continue
        #         if node1 is None or node2 is None:
        #             return False
        #         if node1.val != node2.val:
        #             return False
        #         stack.append((node1.left, node2.left))
        #         stack.append((node1.right, node2.right))
        #     return True

        # if root is None:
        #     return False

        # queue = [root]

        # while queue:
        #     current = queue.pop(0)  # use deque for efficiency

        #     if isSameTree(current, subRoot):
        #         return True

        #     if current.left:
        #         queue.append(current.left)
        #     if current.right:
        #         queue.append(current.right)

        # return False


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


if __name__ == "__main__":
    # Construct the example trees
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)

    subRoot = TreeNode(4)
    subRoot.left = TreeNode(1)
    subRoot.right = TreeNode(2)

    # Print the original trees
    print("Tree root:")
    print_tree(root)
    print("Tree subRoot:")
    print_tree(subRoot)

    # Solution instance
    solution = Solution()

    # Test if subRoot is a subtree of root
    print("Is subRoot a subtree of root?", solution.isSubtree(root, subRoot))  # Output: True

    # Additional test case
    root2 = TreeNode(3)
    root2.left = TreeNode(4)
    root2.right = TreeNode(5)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(2)
    root2.left.right.right = TreeNode(0)

    print("\nTest Case 2:")
    print("Tree root2:")
    print_tree(root2)
    print("Tree subRoot:")
    print_tree(subRoot)
    print("Is subRoot a subtree of root2?", solution.isSubtree(root2, subRoot))  # Output: False
