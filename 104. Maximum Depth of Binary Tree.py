from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    # RECURSIVE DFS
    # Time: O(n), Space: O(1)
    # if not root:
    #   return 0
    # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # BFS
    # Time: O(n), Space: O(1)
    # level = 0
    # q = deque()

    # if root:
    #   q.append(root)

    # while q:
    #   for i in range(len(q)):
    #     node = q.popleft()
    #     if node.left:
    #       q.append(node.left)
    #     if node.right:
    #       q.append(node.right)
    #   level += 1

    # return level

    # ITERATIVE DFS - Preorder(process current node then go to children)
    # Time: O(n), Space: O(n)
    stack = [[root, 1]]
    res = 0

    while stack:
      node, depth = stack.pop()

      if node:
        res = max(res, depth)
        stack.append([node.left, depth + 1])
        stack.append([node.right, depth + 1])
        # stack.extend([[node.left, depth + 1], [node.right, depth + 1]])
        # or
        # stack += [[node.left, depth + 1], [node.right, depth + 1]]
    
    return res


def printTree(node, level=0):
  if node != None:
    printTree(node.left, level + 1)
    print(' ' * 4 * level + '-> ' + str(node.val))
    printTree(node.right, level + 1)



# python3 '.\104. Maximum Depth of Binary Tree.py'
if __name__ == "__main__":
  s = Solution()

  t1 = TreeNode(4, TreeNode(2), TreeNode(7, TreeNode(6), TreeNode(9)))

  printTree(t1)

  p1 = s.maxDepth(t1)

  print(p1)

  assert p1 == 3

