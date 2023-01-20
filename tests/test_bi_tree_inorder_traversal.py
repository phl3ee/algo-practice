"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

"""
import unittest
from algos.bi_tree_inorder_traversal import Solution
from helpers.tree_node import TreeNode

class TestBiTreeInorderTraversal(unittest.TestCase):

    def test_example1(self):
        solution = Solution()
        root =  TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        output = [1,3,2]
        result = solution.inorderTraversal(root)
        self.assertEqual(result, output)

    def test_example2(self):
        solution = Solution()
        root =  []
        output = []
        result = solution.inorderTraversal(root)
        self.assertEqual(result, output)

    def test_example2(self):
        solution = Solution()
        root = TreeNode(1)
        output = [1]
        result = solution.inorderTraversal(root)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()