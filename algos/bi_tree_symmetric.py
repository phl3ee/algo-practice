from typing import Optional
from helpers.tree_node import TreeNode
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        # define a function to compare the supplied tree to itself
        def is_mirror(left, right):
            #if we get to the bottom of the tree we good
            if left is None and right is None:
                return True
            if (left is not None and right is not None):
                #parent node value has to match
                if left.val == right.val:
                    #and the left/right children have to match
                    #simultaneously
                    return (is_mirror(left.left, right.right) and
                            is_mirror(left.right, right.left)
                    )
            #Any mis-match in left/right comparison bubbles out
            return False

        return is_mirror(root, root)
