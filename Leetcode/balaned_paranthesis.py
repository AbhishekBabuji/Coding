"""
The following contains a class and methods
to check for a valid patanthesis
"""
import unittest


class ValidParanthesis:
    """
    The following class contains a static method
    to check for valid paranthesis
    """

    def check_paran(self, input_paran):

        """

        Args:
            input_paran(str): The string for which one must check if it is valid paranthesis

        Returns:
            Boolean (True or False): True of the paranthesis id valid, False otherwise

        """

        openbrace_set = set(('(', '{', '['))
        matching_paran_set = set((('(', ')'), ('{', '}'), ('[', ']')))

        stack = []

        for brace in input_paran:

            if brace in openbrace_set:
                stack.append(brace)

            else:
                if stack:
                    openbrace = stack.pop()
                    closedbrace = brace

                    if tuple((openbrace, closedbrace)) in matching_paran_set:
                        continue

                    else:
                        return False
                else:
                    return False

        return not stack


class Test(unittest.TestCase):
    """
    The class contains test cases to check for valid paranthesis
    """

    def test1(self):
        """
        '()[]{}]'
        False


        """
        example1 = ValidParanthesis()
        self.assertEqual(example1.check_paran('()[]{}]'), False)

    def test2(self):
        """
        '{}['
        False

        """
        example2 = ValidParanthesis()
        self.assertEqual(example2.check_paran('()[]{}'), True)

    def test3(self):
        """
        '('
        False

        """
        example3 = ValidParanthesis()
        self.assertEqual(example3.check_paran('('), False)


if __name__ == '__main__':
    unittest.main()
