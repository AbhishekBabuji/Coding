"""This is a script that
demonstrates how to use unittests
for values returned by instance methods

"""

import unittest


class Solution:

    def addnums(self, a, b):
        return a + b


class TestSolution(unittest.TestCase):

    def test_ex1(self):
        example1 = Solution()
        self.assertEqual(example1.addnums(9, 10), 19)

    def test_ex2(self):
        example2 = Solution()
        self.assertEqual(example2.addnums(5, 10), 15)


if __name__ == '__main__':
    unittest.main()
