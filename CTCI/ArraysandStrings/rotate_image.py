"""You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).


"""
import math
import unittest


class Solution:
    """The class contains an instance method to implement the above algorithm

    """

    def rotate_image(self, mat):

        """


        Args:
            mat (list): a N X N list that must be rotated in place

        Returns:
            mat (list): A 90 degree rotation of the original list
        """

        mat_len = len(mat)

        right_end = mat_len - 1

        start = 0
        stop = math.floor(mat_len / 2) - 1

        left_index = 0
        right_index = mat_len - 1

        while start <= stop:

            for index in range(start, right_index):
                temp = mat[start][index]
                mat[start][index] = mat[right_end - index][start]

                mat[right_end - index][start] = mat[right_end - start][right_end - index]
                mat[right_end - start][right_end - index] = mat[right_end - (right_end - index)][right_end - start]
                mat[right_end - (right_end - index)][right_end - start] = temp

            start += 1
            right_index -= 1

        return mat


class TestSolution(unittest.TestCase):
    """Class that implements test cases

    """

    def test_ex1(self):
        """
        Test case 1:

        [[5, 1, 9, 11],[2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]] must return
        [[15, 13, 2, 5],[14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
        """

        example1 = Solution()
        self.assertEqual(example1.rotate_image([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]),
                         [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]])

    def test_ex2(self):
        """
        Test case 2:

        [[1, 2, 3], [4, 5, 6], [7, 8, 9]] must return [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        """

        example2 = Solution()
        self.assertEqual(example2.rotate_image([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                         [[7, 4, 1], [8, 5, 2], [9, 6, 3]])


if __name__ == '__main__':
    unittest.main()
