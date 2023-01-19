"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

"""
import unittest
from algos.addTwoNumbers import Solution
from helpers.listNodeHelpers import ListNode

class TestAddTwoNumbers(unittest.TestCase):

    def test_example1(self):
        helper = ListNode()
        solution = Solution()
        l1 = helper.buildListNodeFromList([2,4,3])
        l2 = helper.buildListNodeFromList([5,6,4])
        output = [7,0,8]
        result = solution.addTwoNumbers(l1, l2)
        self.assertEqual(result.val, output[0])
        self.assertEqual(result.next.val, output[1])
        self.assertEqual(result.next.next.val, output[2])

    def test_example2(self):
        helper = ListNode()
        solution = Solution()
        l1 = helper.buildListNodeFromList([0])
        l2 = helper.buildListNodeFromList([0])
        output = [0]
        result = solution.addTwoNumbers(l1, l2)
        self.assertEqual(result.val, output[0])

    def test_example3(self):
        helper = ListNode()
        solution = Solution()
        l1 = helper.buildListNodeFromList([9,9,9,9,9,9,9])
        l2 = helper.buildListNodeFromList([9,9,9,9])
        output = [8,9,9,9,0,0,0,1]
        result = solution.addTwoNumbers(l1, l2)
        convertResult = helper.buildListFromListNode(result)
        self.assertEqual(convertResult, output)


if __name__ == '__main__':
    unittest.main()