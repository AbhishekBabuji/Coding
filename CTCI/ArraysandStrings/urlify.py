"""
Write a method to replace all spaces in a string with %20

Note that this is an awkward exercise to do in Python,
or any language in which strings are immutable.
Since you can't perform the substitutions in place,
you have to return a copy, which means that the
minimum space requirement is O(n)



"""
import unittest


class Solution:
    """Provides an instance method 'urlify()' to implement the required algorithm


    """

    def urlify(self, inputstring):
        """

        Args:
            inputstring (str): Input string which has may or may not have spaces

        Returns:
            inputstring (str): Input string with spaces replaced by '%20'
        """

        return inputstring.replace(" ", "%20")


class TestSolution(unittest.TestCase):
    """Test cases for instances of Solution class


    """

    def test_ex1(self):
        """

        Test case 1: "Omega      lul"
        """

        example1 = Solution()
        self.assertEqual(example1.urlify("Omega      lul"), "Omega%20%20%20%20%20%20lul")

    def test_ex2(self):
        """

        Test case 1: "  Omegalul"
        """

        example2 = Solution()
        self.assertEqual(example2.urlify("  Omegalul"), "%20%20Omegalul")

    def test_ex3(self):
        """

        Test case 1: "Omegalul"
        """

        example3 = Solution()
        self.assertEqual(example3.urlify("Omegalul"), "Omegalul")


if __name__ == '__main__':
    unittest.main()
