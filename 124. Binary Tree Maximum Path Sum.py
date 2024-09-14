# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # Initialize the variable to store the maximum path sum
        self.max_sum = root.val  # float('-inf')
        # max_sum = [root.val]

        # Helper function to compute maximum path sum for each node
        def dfs(node):
            if node is None:
                return 0

            # Recursively compute the maximum contribution of left and right children
            left_max = dfs(node.left)
            left_max = max(left_max, 0)  # Only add positive gains
            right_max = dfs(node.right)
            right_max = max(right_max, 0)  # Only add positive gains

            current_max_path = node.val + left_max + right_max
            self.max_sum = max(self.max_sum, current_max_path)
            # max_sum[0] = max(max_sum[0], current_max_path)

            # Return the maximum gain if we continue from the current node
            return node.val + max(left_max, right_max)

        # Start the recursion from the root
        dfs(root)

        # Return the result
        return self.max_sum  # max_sum[0]


# Helper function to print the tree in order (for testing purposes)
def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.val, end=" ")
        print_inorder(root.right)


# Example Usage
if __name__ == "__main__":
    # Construct a sample binary tree
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # Solution instance
    solution = Solution()
    print_inorder(root)
    print()
    # Get the maximum path sum
    print(f"Maximum Path Sum: {solution.maxPathSum(root)}")  # Output: 42
