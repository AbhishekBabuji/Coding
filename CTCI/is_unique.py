"""Implement an algorithm to determine if a string
has all unique characters. What if you cannot use additional
data structures?

"""

import unittest


class Solution:
    """

    This is a Solution class, a means by which you can create instances
    and pass each test case as an instance of this class.
    It has one instance method which implements
    the intended algoritm


    """

    def is_unique(self, input_string):
        """
        A method to check if an input string has all unique characters.


        Args:
            input_string (str): The input string which must be checked for the presence
                                of all unique characters

        Returns:
            Boolean: True if the string has all unique characters, False if otherwise
        """

        input_string_set = set(input_string)

        return len(input_string) == len(input_string_set)


class TestSolution(unittest.TestCase):
    """A class that implements a few test cases


    """

    def test_ex1(self):
        example1 = Solution()
        self.assertEqual(example1.is_unique('abhishek'), False)

    def test_ex2(self):
        example2 = Solution()
        self.assertEqual(example2.is_unique('a'), True)

    def test_ex3(self):
        example3 = Solution()
        self.assertEqual(example3.is_unique('mepo'), True)


if __name__ == '__main__':
    unittest.main()
