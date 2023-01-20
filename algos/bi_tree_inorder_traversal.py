# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
from helpers.tree_node import TreeNode

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        #Leave if there is nothing for us
        if root == None:
            return output

        #Go Left first
        if root:
            output = self.inorderTraversal(root.left)
            output.append(root.val)
            output = output + self.inorderTraversal(root.right)

        return output