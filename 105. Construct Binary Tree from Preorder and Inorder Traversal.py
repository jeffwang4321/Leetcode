# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder):
        # # Approach 1 - Stack
        # if preorder is None or inorder is None:
        #     return None

        # root = TreeNode(preorder[0])
        # stack = [root]
        # inorder_index = 0

        # for i in range(1, len(preorder)):
        #     current_val = preorder[i]
        #     node = stack[-1]

        #     if node.val != inorder[inorder_index]:
        #         node.left = TreeNode(current_val)
        #         stack.append(node.left)
        #     else:
        #         while stack and stack[-1].val == inorder[inorder_index]:
        #             node = stack.pop()
        #             inorder_index += 1

        #         node.right = TreeNode(current_val)
        #         stack.append(node.right)

        # return root

        # # Approach 2 - Recursive
        # inorder_index_map = {value: index for index, value in enumerate(inorder)}

        # def buildTreeHelper(preorder_start, preorder_end, inorder_start, inorder_end):
        #     if preorder_start > preorder_end:
        #         return None

        #     root_val = preorder[preorder_start]
        #     root = TreeNode(root_val)

        #     inorder_index = inorder_index_map[root_val]

        #     left_subtree_size = inorder_index - inorder_start

        #     root.left = buildTreeHelper(
        #         preorder_start + 1, preorder_start + left_subtree_size, inorder_start, inorder_index - 1
        #     )
        #     root.right = buildTreeHelper(
        #         preorder_start + left_subtree_size + 1, preorder_end, inorder_index + 1, inorder_end
        #     )

        #     return root

        # return buildTreeHelper(0, len(preorder) - 1, 0, len(inorder) - 1)

        # # Approach - easy
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        return root


# Helper function to print the tree in order (for testing purposes)
def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.val, end=" ")
        print_inorder(root.right)


# Example Usage
if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    solution = Solution()
    root = solution.buildTree(preorder, inorder)

    # Print the constructed binary tree in inorder
    print("Constructed Binary Tree Inorder Traversal: ")
    print_inorder(root)  # Output should match the original inorder list
