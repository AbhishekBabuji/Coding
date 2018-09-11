"""Given two strings, write a method to check
if one string is a permutation of the other


"""
import unittest


class Solution:
    """

    This class can be used to create instances of test cases to
    check if the indented algorithm is implemented correctly

    """

    def check_perm(self, input_string1, input_string2):

        """

        Args:
            input_string1 (str): First string to be compared
            input_string2 (str): Second string to be compared



        Returns:

            Boolean: True if one string is a permutation of another


        """

        freq_dict = {}

        for string_index in range(0, len(input_string1)):

            if not freq_dict.get(input_string1[string_index]):
                freq_dict[input_string1[string_index]] = 1

            else:
                freq_dict[input_string1[string_index]] += 1

        for string_index in range(0, len(input_string2)):

            if not freq_dict.get(input_string2[string_index]):
                return False

            freq_dict[input_string2[string_index]] -= 1

        return all(value == 0 for value in freq_dict.values())


class TestSolution(unittest.TestCase):
    """Unit Testing for instances of Solution()

    """

    def test_ex1(self):
        """
        First test case: 'panorama', 'ramanopa'
        """

        example1 = Solution()
        self.assertEqual(example1.check_perm('panorama', 'ramanopa'), True)

    def test_ex2(self):
        """
        Second test case: 'pano', 'pan'
        """

        example2 = Solution()
        self.assertEqual(example2.check_perm('pano', 'pan'), False)

    def test_ex3(self):
        """
        Third test case: 'p', 'q'
        """

        example3 = Solution()
        self.assertEqual(example3.check_perm('p', 'q'), False)

    def test_ex4(self):
        """
        Third test case: 'pqr', 'qpr'
        """

        example4 = Solution()
        self.assertEqual(example4.check_perm('pqr', 'qpr'), True)


if __name__ == '__main__':
    unittest.main()
