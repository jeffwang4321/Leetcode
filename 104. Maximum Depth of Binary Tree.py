from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # # RECURSIVE DFS
        # # Time: O(n), Space: O(1)
        # if root is None:
        #     return 0

        # left_depth = self.maxDepth(root.left)
        # right_depth = self.maxDepth(root.right)
        # return max(left_depth, right_depth) + 1

        # # BFS
        # # Time: O(n), Space: O(1)
        if root is None:
            return 0

        depth = 0
        q = deque([root])

        while q:
            depth += 1
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        return depth

        # ITERATIVE DFS - Preorder(process current node then go to children)
        # Time: O(n), Space: O(n)
        # stack = [[root, 1]]
        # res = 0

        # while stack:
        #     node, depth = stack.pop()

        #     if node:
        #         res = max(res, depth)
        #         stack.append([node.left, depth + 1])
        #         stack.append([node.right, depth + 1])
        #         # stack.extend([[node.left, depth + 1], [node.right, depth + 1]])
        #         # or
        #         # stack += [[node.left, depth + 1], [node.right, depth + 1]]

        # return res


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
    # Example tree:
    #      3
    #     / \
    #    9  20
    #       / \
    #      15  7

    # Creating the example tree
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # Print the original tree
    print("Original tree:")
    print_tree(root)

    # Solution instance
    solution = Solution()

    # Test maximum depth calculation
    print("Maximum Depth:", solution.maxDepth(root))  # Output: 3

    # Additional test case 1
    print("\nTest Case 1:")
    # Tree: 1 -> (None, 2 -> (None, 3))
    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    root1.right.right = TreeNode(3)
    print("Original:", end=" ")
    print_tree(root1)
    print("Maximum Depth:", solution.maxDepth(root1))  # Output: 3

    # Additional test case 2 (single node)
    print("\nTest Case 2:")
    root2 = TreeNode(1)
    print("Original:", end=" ")
    print_tree(root2)
    print("Maximum Depth:", solution.maxDepth(root2))  # Output: 1

    # Additional test case 3 (empty tree)
    print("\nTest Case 3:")
    root3 = None
    print("Original:", end=" ")
    print_tree(root3)
    print("Maximum Depth:", solution.maxDepth(root3))  # Output: 0
