"""
Test with: python -m unittest tests.test_bi_tree_symmetric -v
e.g. python -m unittest tests.test_longest_common_prefix -v

Given the root of a binary tree, check whether it is a mirror of itself
(i.e., symmetric around its center).


Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false

"""
import unittest
from algos.bi_tree_symmetric import Solution
from helpers.tree_node import TreeNode

class Test_isSymmetric(unittest.TestCase):
    """ Unit tests for leetcode fun and games
    """

    def test_example1(self):
        """Example case from leetcode
        """
        test   = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right = TreeNode(2)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(3)
        output = True
        result = test.isSymmetric(root)
        self.assertEqual(result, output)

    def test_example2(self):
        """Example case from leetcode
        """
        test   = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = TreeNode(3)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        output = False
        result = test.isSymmetric(root)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()