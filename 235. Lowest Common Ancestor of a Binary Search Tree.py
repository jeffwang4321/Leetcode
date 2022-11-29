from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    # Time: O(logn) - visit 1 node per level, Space: O(1) - no data structures
    cur = root

    while cur:
      if p.val > cur.val and q.val > cur.val:
        cur = cur.right
      elif p.val < cur.val and q.val < cur.val:
        cur = cur.left
      else:
        return cur


def printTree(node, level=0):
  if node != None:
    printTree(node.left, level + 1)
    print(' ' * 4 * level + '-> ' + str(node.val))
    printTree(node.right, level + 1)



# python3 '.\235. Lowest Common Ancestor of a Binary Search Tree.py'
if __name__ == "__main__":
  s = Solution()

  t1 = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))

  printTree(t1)

  p1 = s.lowestCommonAncestor(t1, TreeNode(2), TreeNode(8)).val

  print(p1)

  assert p1 == 6

