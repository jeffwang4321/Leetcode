# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    # # Approach 1 - Dfs
    # def serialize(self, root):
    #     """Encodes a tree to a single string using DFS."""

    #     def dfs(node):
    #         if not node:
    #             result.append("null")
    #             return
    #         result.append(str(node.val))
    #         dfs(node.left)
    #         dfs(node.right)

    #     result = []
    #     dfs(root)
    #     return ",".join(result)

    # def deserialize(self, data):
    #     """Decodes your encoded data to tree using DFS."""

    #     def dfs():
    #         if self.data[self.index] == "null":
    #             self.index += 1
    #             return None

    #         node = TreeNode(int(self.data[self.index]))
    #         self.index += 1
    #         node.left = dfs()
    #         node.right = dfs()
    #         return node

    #     # Split the data into nodes' values
    #     self.data = data.split(",")
    #     self.index = 0
    #     return dfs()

    # # Approach 2 - BFS and stack
    def serialize(self, root):
        """Encodes a tree to a single string."""
        if not root:
            return "null"

        # Initialize the queue for BFS
        queue = [root]
        result = []

        while queue:
            node = queue.pop(0)
            if node:
                result.append(str(node.val))  # Serialize current node value
                queue.append(node.left)  # Enqueue left child
                queue.append(node.right)  # Enqueue right child
            else:
                result.append("null")  # Serialize 'null' for missing nodes

        # Join all elements with commas to form the serialized string
        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        if data == "null":
            return None

        # Split the data into nodes' values
        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))  # Root is the first element
        queue = [root]
        index = 1

        while queue:
            node = queue.pop(0)

            # Deserialize left child
            if nodes[index] != "null":
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1

            # Deserialize right child
            if nodes[index] != "null":
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1

        return root


# Example Usage
if __name__ == "__main__":
    # Construct a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    # Instantiate Codec object
    codec = Codec()

    # Serialize the tree
    serialized_data = codec.serialize(root)
    print(f"Serialized: {serialized_data}")  # Output: "1,2,null,null,3,4,null,null,5,null,null"

    # Deserialize the string back to the tree
    deserialized_tree = codec.deserialize(serialized_data)

    # Check if the deserialization was successful by serializing it again
    print(f"Deserialized and then Serialized: {codec.serialize(deserialized_tree)}")
    # Output should match the original serialization
