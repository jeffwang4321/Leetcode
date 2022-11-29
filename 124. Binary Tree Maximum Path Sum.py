from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Time: O(n) - traverse all nodes get max path
        res = [root.val] # use list, works as global variable

        # return max path without split
        def dfs(root):
            if not root: # if not None
                return 0
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0) # choose 0, if negative
            rightMax = max(rightMax, 0) 
            
            # compute max path sum WITH split to global res
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # return max path sum WITHOUT split to recursive DFS
            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]


def printTree(node, level=0):
  if node != None:
    printTree(node.left, level + 1)
    print(' ' * 4 * level + '-> ' + str(node.val))
    printTree(node.right, level + 1)



# python3 '.\124. Binary Tree Maximum Path Sum.py'
if __name__ == "__main__":
  s = Solution()

  t1 = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

  printTree(t1)
  r1 = s.maxPathSum(t1)

  print(r1)

  assert r1 == 42



