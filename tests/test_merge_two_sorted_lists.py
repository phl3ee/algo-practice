"""
Test with: python -m unittest tests.<test_Case> -v
e.g. python -m unittest tests.test_longest_common_prefix -v

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.


Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

"""
import unittest
from algos.list_node_merge_sorted_lists import Solution
from helpers.listNodeHelpers import ListNode

class Test_sorted_lists(unittest.TestCase):

    def test_example1(self):
        test   = Solution()
        listHelper = ListNode()
        list1 = listHelper.buildListNodeFromList([1,2,4])
        list2 = listHelper.buildListNodeFromList([1,3,4])
        output = [1,1,2,3,4,4]
        result = test.mergeTwoLists(list1, list2)
        theirResult = listHelper.buildListFromListNode(result)
        self.assertEqual(theirResult, output)

    def test_example2(self):
        # this test case is BS blackbox crazyness on leetcode
        test   = Solution()
        listHelper = ListNode()
        list1 = []
        list2 = []
        output = []
        result = test.mergeTwoLists(list1, list2)
        self.assertEqual(result.val, '')

    def test_example3(self):
        test   = Solution()
        listHelper = ListNode()
        list1 = []
        list2 = ListNode()
        output = [0]
        result = test.mergeTwoLists(list1, list2)
        theirResult = listHelper.buildListFromListNode(result)
        self.assertEqual(theirResult, output)

if __name__ == '__main__':
    unittest.main()