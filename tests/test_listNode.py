"""
Testing listNode helpers
"""
import unittest
from helpers.listNodeHelpers import ListNode

class TestListNode(unittest.TestCase):

    def test_ListToNodes(self):
        test = ListNode()
        list = [2,4,3]
        output = [2,4,3]
        result = test.buildListNodeFromList(list)
        self.assertEqual(result.val, output[0])
        self.assertEqual(result.next.val, output[1])
        self.assertEqual(result.next.next.val, output[2])

    def test_NodesToList(self):
        test = ListNode()
        input = ListNode(1,next=ListNode())
        #print(input.val,input.next.val)
        output = [1,0]
        result = test.buildListFromListNode(input)
        self.assertEqual(result, output)


if __name__ == '__main__':
    unittest.main()