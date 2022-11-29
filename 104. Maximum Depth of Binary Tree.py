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



# python3 '.\104. Maximum Depth of Binary Tree.py'
if __name__ == "__main__":
  s = Solution()

  t1 = TreeNode(4, TreeNode(2), TreeNode(7, TreeNode(6), TreeNode(9)))

  traverse(t1)

  print("maxDepth =", s.maxDepth(t1))

