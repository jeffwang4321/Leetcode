from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
      return None

    # swap the children
    temp = root.left
    root.left = root.right
    root.right = temp

    self.invertTree(root.left)
    self.invertTree(root.right)
    return root

def printTree(node, level=0):
  if node != None:
    printTree(node.left, level + 1)
    print(' ' * 4 * level + '-> ' + str(node.val))
    printTree(node.right, level + 1)

def traverse(root):
  current_level = [root]
  while current_level:
    print(' '.join(str(node.val) for node in current_level))
    next_level = list()
    for n in current_level:
      if n.left:
        next_level.append(n.left)
      if n.right:
        next_level.append(n.right)
    current_level = next_level



# python3 '.\226. Invert Binary Tree.py'
if __name__ == "__main__":
  s = Solution()

  t1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))

  traverse(t1)
  # printTree(t1)

  traverse(s.invertTree(t1))

