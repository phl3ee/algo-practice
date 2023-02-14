from typing import Optional
from helpers.tree_node import TreeNode
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0
        else:
            left_depth  = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)

        if (left_depth > right_depth):
            return left_depth + 1
        else:
            return right_depth + 1

    def maxDepth_fast1(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1