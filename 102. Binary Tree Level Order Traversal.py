# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        # # Approach 1 - deque
        # if root is None:
        #     return []

        # result = []
        # queue = deque([root])

        # while queue:
        #     level_values = []

        #     for _ in range(len(queue)):
        #         node = queue.popleft()
        #         level_values.append(node.val)

        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)

        #     result.append(level_values)

        # return result

        # # Approach 2 - recursion

        result = []

        def traverse(node: TreeNode, level: int):
            if node is None:
                return

            if len(result) <= level:
                result.append([])

            result[level].append(node.val)

            traverse(node.left, level + 1)
            traverse(node.right, level + 1)

        traverse(root, 0)
        return result


# Helper function to print tree (for testing)
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


# Test cases
if __name__ == "__main__":
    # Construct the example tree
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # Print the original tree
    print("Tree root:")
    print_tree(root)

    # Solution instance
    solution = Solution()

    # Perform level order traversal
    levels = solution.levelOrder(root)
    print("Level order traversal:")
    print(levels)
