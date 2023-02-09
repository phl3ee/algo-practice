"""
Test with: python -m unittest tests.<test_Case> -v
e.g. python -m unittest tests.test_longest_common_prefix -v

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

"""
import unittest
from algos.valid_parentheses import Solution

class Test_Valid_Parentheses(unittest.TestCase):

    def test_example1(self):
        test   = Solution()
        s      = "()"
        output = True
        result = test.isValid(s)
        self.assertEqual(result, output)

    def test_example2(self):
        test   = Solution()
        s      = "()[]{}"
        output = True
        result = test.isValid(s)
        self.assertEqual(result, output)

    def test_example3(self):
        test   = Solution()
        s      = "(]"
        output = False
        result = test.isValid(s)
        self.assertEqual(result, output)

    def test_uneven_input(self):
        test   = Solution()
        s      = "]"
        output = False
        result = test.isValid(s)
        self.assertEqual(result, output)

    def test_just_closes(self):
        test   = Solution()
        s      = "]]"
        output = False
        result = test.isValid(s)
        self.assertEqual(result, output)

    def test_nested_fatfinger(self):
        test   = Solution()
        s      = "((([([]])"
        output = False
        result = test.isValid(s)
        self.assertEqual(result, output)

    def test_i_used_LISP_at_uni(self):
        test   = Solution()
        s      = "((()())())"
        output = True
        result = test.isValid(s)
        self.assertEqual(result, output)

    def test_example5(self):
        test   = Solution()
        s      = "([)]"
        output = False
        result = test.isValid(s)
        self.assertEqual(result, output)

    def test_example6(self):
        test   = Solution()
        s      = "([])"
        output = True
        result = test.isValid(s)
        self.assertEqual(result, output)

    def test_just_opens(self):
        test   = Solution()
        s      = "(("
        output = False
        result = test.isValid(s)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()