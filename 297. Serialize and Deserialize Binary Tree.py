from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Codec:
    # Preorder 
    # Time: O(n), Space: O(n)
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    # Preorder 
    # Time: O(n), Space: O(1)
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()


def printTree(node, level=0):
  if node != None:
    printTree(node.left, level + 1)
    print(' ' * 4 * level + '-> ' + str(node.val))
    printTree(node.right, level + 1)



# python3 '.\297. Serialize and Deserialize Binary Tree.py'
if __name__ == "__main__":
  s = Codec()

  t1 = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

  printTree(t1)
  r1 = s.serialize(t1)
  print(r1)
  assert r1 == '-10,9,N,N,20,15,N,N,7,N,N'

  r2 = s.deserialize(r1)
  printTree(r2)
  



