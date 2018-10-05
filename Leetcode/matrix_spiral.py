"""
Print matrix in spiral order
"""
import unittest
import numpy as np


class Solution:
    """
    Contains a class that has functions to print
    the elements of a matrix in spiral order
    """

    def change_dir(self, curr_dir):

        """
        Args:
            curr_dir (str): Represents the current direction


        Returns:
            (str): Changed direction based on the current direction

        """

        if curr_dir == 'ltr':
            return 'ttb'

        elif curr_dir == 'ttb':
            return 'rtl'

        elif curr_dir == 'rtl':
            return 'btt'
        return 'ltr'

    def check_stop_cond(self, curr_dir, visited_set, i, j):

        """

        Args:
            curr_dir (str): Represents the current direction
            visited_set (set): Represents the left and right indices in the set
            i (int): Represents the left index
            j (int): Represents the right index


        Returns:
            (str): Changed direction based on the current direction

        """

        if curr_dir == 'ltr':
            return not (i + 1, j) in visited_set

        elif curr_dir == 'ttb':
            return not (i, j - 1) in visited_set

        elif curr_dir == 'rtl':
            return not (i - 1, j) in visited_set

        return not (i, j + 1) in visited_set

    def matrix_spiral(self, input_matrix):

        """
        Args:
            input_matrix (list of lists): 2D lists


        Returns:
            spiral_elements (list): Returns the elements of input_list in spiral_order

        """

        num_rows = np.shape(input_matrix)[0]
        num_cols = np.shape(input_matrix)[1]
        i = 0
        j = 0
        visited_set = {(0, 0), (0, num_cols), (num_rows, num_cols - 1), (num_rows - 1, -1)}

        spiral_elements = [input_matrix[0][0]]
        stop_cond = False
        curr_dir = "ltr"

        while not stop_cond:

            if curr_dir == "ltr":

                if (i, j + 1) not in visited_set:
                    j += 1
                    visited_set.add((i, j))
                    spiral_elements.append(input_matrix[i][j])

                else:
                    if self.check_stop_cond(curr_dir, visited_set, i, j):
                        new_dir = self.change_dir(curr_dir)
                        curr_dir = new_dir

                    else:
                        stop_cond = True
                        break

            elif curr_dir == "ttb":

                if (i + 1, j) not in visited_set:
                    i += 1
                    visited_set.add((i, j))
                    spiral_elements.append(input_matrix[i][j])

                else:
                    if self.check_stop_cond(curr_dir, visited_set, i, j):
                        new_dir = self.change_dir(curr_dir)
                        curr_dir = new_dir

                    else:
                        stop_cond = True
                        break

            elif curr_dir == "rtl":

                if (i, j - 1) not in visited_set:
                    j -= 1
                    visited_set.add((i, j))
                    spiral_elements.append(input_matrix[i][j])

                else:
                    if self.check_stop_cond(curr_dir, visited_set, i, j):
                        new_dir = self.change_dir(curr_dir)
                        curr_dir = new_dir

                    else:
                        stop_cond = True
                        break

            else:
                if (i - 1, j) not in visited_set:
                    i -= 1
                    visited_set.add((i, j))
                    spiral_elements.append(input_matrix[i][j])

                else:
                    if self.check_stop_cond(curr_dir, visited_set, i, j):
                        new_dir = self.change_dir(curr_dir)
                        curr_dir = new_dir

                    else:
                        stop_cond = True
                        break

        return spiral_elements


class TestSolution(unittest.TestCase):
    """Class that implements test cases

    """

    def test1(self):
        """
        Test case 1:

        [[1, 2, 3], [4, 5, 6], [7, 8, 9]] must return
        [1, 2, 3, 6, 9, 8, 7, 4, 5]
        """
        example1 = Solution()
        self.assertEqual(example1.matrix_spiral([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                         [1, 2, 3, 6, 9, 8, 7, 4, 5])

    def test2(self):
        """
        Test case 2:

        [[1, 2, 3], [4, 5, 6]] must return
        [1, 2, 3, 6, 5, 4]
        """
        example2 = Solution()
        self.assertEqual(example2.matrix_spiral([[1, 2, 3], [4, 5, 6]]),
                         [1, 2, 3, 6, 5, 4])

    def test3(self):
        """
        Test case 3:

        [[1], [2], [3]] must return
        [1, 2, 3]
        """
        example3 = Solution()
        self.assertEqual(example3.matrix_spiral([[1], [2], [3]]),
                         [1, 2, 3])

    def test4(self):
        """
        Test case 4:

        [[1]] must return
        [1]
        """
        example4 = Solution()
        self.assertEqual(example4.matrix_spiral([[1]]),
                         [1])


if __name__ == '__main__':
    unittest.main()
