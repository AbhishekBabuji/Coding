"""Implement an algorithm to determine one of three types of edits
1. Insert a character
2. Remove a character
3. Replace a character

"""
import unittest


class Solution:
    """
    A class which has the instance methods to implement
    the algorithm above

    """

    def one_away(self, inputstring1, inputstring2):

        """


        Args:
            inputstring1 (str): string 1 which may be longer than or equal to string 2
            inputstring2 (str): string 2 which may be longer than or equal to string 1

        Returns:
            boolean: True if the two strings differ by 1 or less edits away. False, otherwise.

        """

        if abs(len(inputstring2) - len(inputstring1)) <= 1:

            if len(inputstring1) > len(inputstring2):
                return len(set(inputstring1) - set(inputstring2)) <= 1

            return len(set(inputstring2) - set(inputstring1)) <= 1

        return False


class TestSolution(unittest.TestCase):
    """Class containing test cases

    """

    def test_ex1(self):
        """Test case 1: 'pale', 'ple'

        """

        example1 = Solution()
        self.assertEqual(example1.one_away('pale', 'ple'), True)

    def test_ex2(self):
        """Test case 2: 'pales', 'ple'

        """

        example2 = Solution()
        self.assertEqual(example2.one_away('pales', 'ple'), False)

    def test_ex3(self):
        """Test case 3: 'pales', 'pale'

        """
        example3 = Solution()
        self.assertEqual(example3.one_away('pales', 'pale'), True)

    def test_ex4(self):
        """Test case 4: 'pales', 'palesab'

        """
        example4 = Solution()
        self.assertEqual(example4.one_away('pales', 'palesab'), False)

    def test_ex5(self):
        """Test case 4: 'pale', 'bale'

        """
        example5 = Solution()
        self.assertEqual(example5.one_away('pale', 'bale'), True)

    def test_ex6(self):
        """Test case 4: 'pale', 'bake'

        """

        example6 = Solution()
        self.assertEqual(example6.one_away('pale', 'bake'), False)


if __name__ == '__main__':
    unittest.main()
