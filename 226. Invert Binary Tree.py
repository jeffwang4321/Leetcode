from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # # Method 1 - Recursion
        if root is None:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

        # # Method 2 - deque
        # if root is None:
        #     return None

        # queue = deque([root])
        # while queue:
        #     curr = queue.popleft()

        #     curr.left, curr.right = curr.right, curr.left

        #     if curr.left:
        #         queue.append(curr.left)
        #     if curr.right:
        #         queue.append(curr.right)

        # return root


# Helper function to print the binary tree in level order (BFS) for easy comparison
def print_tree(root: TreeNode):
    if not root:
        print("None")
        return

    queue = [root]
    result = []

    while queue:
        current = queue.pop(0)
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


# python3 '.\226. Invert Binary Tree.py'
if __name__ == "__main__":
    # Example tree:
    #      4
    #     / \
    #    2   7
    #   / \ / \
    #  1  3 6  9

    # Creating the example tree
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    # Print the original tree
    print("Original tree:")
    print_tree(root)

    # Invert the binary tree
    solution = Solution()
    inverted_root = solution.invertTree(root)

    # Print the inverted tree
    print("\nInverted tree:")
    print_tree(inverted_root)

    # Additional test case 1
    print("\nTest Case 1:")
    # Tree: 1 -> (2, 3)
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    print("Original:", end=" ")
    print_tree(root1)
    inverted_root1 = solution.invertTree(root1)
    print("Inverted:", end=" ")
    print_tree(inverted_root1)

    # Additional test case 2
    print("\nTest Case 2:")
    # Tree: 1
    root2 = TreeNode(1)
    print("Original:", end=" ")
    print_tree(root2)
    inverted_root2 = solution.invertTree(root2)
    print("Inverted:", end=" ")
    print_tree(inverted_root2)

    # Additional test case 3 (Empty tree)
    print("\nTest Case 3:")
    # Tree: None
    root3 = None
    print("Original:", end=" ")
    print_tree(root3)
    inverted_root3 = solution.invertTree(root3)
    print("Inverted:", end=" ")
    print_tree(inverted_root3)
