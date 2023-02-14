"""
Test with: python -m unittest tests.test_bi_tree_maxdepth -v
e.g. python -m unittest tests.test_longest_common_prefix -v

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the
longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]

Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

"""
import unittest
from algos.bi_tree_maxdepth import Solution
from helpers.tree_node import TreeNode

class Test_maxDepth(unittest.TestCase):
    """ Unit tests for leetcode fun and games
    """

    def test_example1(self):
        solution = Solution()
        root =  TreeNode(3)
        root.left =  TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        output = 3
        result = solution.maxDepth(root)
        self.assertEqual(result, output)

    def test_example2(self):
        solution = Solution()
        root =  TreeNode(1)
        root.right = TreeNode(2)
        output = 2
        result = solution.maxDepth(root)
        self.assertEqual(result, output)

    def test_example1_fast1(self):
        solution = Solution()
        root =  TreeNode(3)
        root.left =  TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        output = 3
        result = solution.maxDepth_fast1(root)
        self.assertEqual(result, output)

    def test_example2_fast1(self):
        solution = Solution()
        root =  TreeNode(1)
        root.right = TreeNode(2)
        output = 2
        result = solution.maxDepth_fast1(root)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()