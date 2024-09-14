# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # # Approach - Min/Max Bounds Approach
        # def validate(node, low=float("-inf"), high=float("inf")):
        #     if node is None:
        #         return True

        #     if node.val <= low or node.val >= high:
        #         return False

        #     return (validate(node.left, low, node.val)) and (validate(node.right, node.val, high))

        # return validate(root)

        # # Approach - In order Traversal

        stack = []
        prev_val = float("-inf")

        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            if curr.val <= prev_val:
                return False

            prev_val = curr.val

            curr = curr.right

        return True


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
    # Construct a valid BST
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    # Print the original tree
    print("Tree root:")
    print_tree(root)

    # Solution instance
    solution = Solution()

    # Validate the BST
    is_valid = solution.isValidBST(root)
    print(f"Is the tree a valid BST? {is_valid}")

    # Construct an invalid BST
    root_invalid = TreeNode(5)
    root_invalid.left = TreeNode(1)
    root_invalid.right = TreeNode(4)
    root_invalid.right.left = TreeNode(3)
    root_invalid.right.right = TreeNode(6)

    # Print the invalid tree
    print("Invalid Tree root:")
    print_tree(root_invalid)

    # Validate the invalid BST
    is_valid = solution.isValidBST(root_invalid)
    print(f"Is the tree a valid BST? {is_valid}")
