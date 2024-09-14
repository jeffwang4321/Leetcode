# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr

        return None


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
    # Construct the example trees
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)

    p = root.left  # Node with value 2
    q = root.left.right  # Node with value 4

    # Print the original tree
    print("Tree root:")
    print_tree(root)

    # Solution instance
    solution = Solution()

    # Find the lowest common ancestor
    lca = solution.lowestCommonAncestor(root, p, q)
    print(f"The lowest common ancestor of nodes {p.val} and {q.val} is: {lca.val if lca else None}")

    # Additional test case
    p = root.left  # Node with value 2
    q = root.right  # Node with value 8

    lca = solution.lowestCommonAncestor(root, p, q)
    print(f"The lowest common ancestor of nodes {p.val} and {q.val} is: {lca.val if lca else None}")
