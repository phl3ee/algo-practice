"""
Try and get some TreeNode action going
"""
import unittest
from helpers.tree_node import TreeNode

class TestTreeNode(unittest.TestCase):

    def test_LevelOrderTraversal(self):
        test = TreeNode()

        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)

        output = [1,2,3]
        result = test.levelorder(root)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()