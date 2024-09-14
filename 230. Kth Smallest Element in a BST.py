# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # # Apraoch 1 - Stack
        # stack = []
        # curr = root

        # while curr or stack:
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left

        #     curr = stack.pop()
        #     k -= 1

        #     if k == 0:
        #         return curr.val

        #     curr = curr.right

        # return -1

        # # Approach 2 - Recursive
        # count = 0
        # result = None
        def inorder_traversal(node):
            # nonlocal count, result

            if node is None:
                return

            inorder_traversal(node.left)

            self.count += 1
            if self.count == k:
                self.result = node.val
                return

            inorder_traversal(node.right)

        self.count = 0
        inorder_traversal(root)

        return self.result


# Helper function to print tree (for testing)
def print_tree(root):
    if not root:
        print("None")
        return

    queue = [root]
    front = 0
    result = []

    while front < len(queue):
        current = queue[front]
        front += 1
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


# Test cases
if __name__ == "__main__":
    # Construct a BST
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)

    # Print the original tree
    print("Tree root:")
    print_tree(root)

    # Solution instance
    solution = Solution()

    # Test finding k-th smallest elements
    k = 1
    print(f"The {k}th smallest element in the BST is: {solution.kthSmallest(root, k)}")

    k = 2
    print(f"The {k}th smallest element in the BST is: {solution.kthSmallest(root, k)}")

    k = 3
    print(f"The {k}th smallest element in the BST is: {solution.kthSmallest(root, k)}")

    k = 4
    print(f"The {k}th smallest element in the BST is: {solution.kthSmallest(root, k)}")
