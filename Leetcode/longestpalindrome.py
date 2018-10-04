"""
Given a string which consists of lowercase or uppercase letters,
find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

"""

import unittest


class Solution:
    """
    The class contains methods to implement the longest palindrome problem

    """

    def check_pal(potential_pal):

        if potential_pal[::-1] == potential_pal:
            return True

        return False

    def longest_palindrome(input_string):
        """

        Args:
            input_string (str):

        Returns:

            longest_pal (int): Length of the longest palindrome

        """
        potential_candidates = []
        freq_dict = {}
        current_sequence = ""

        for char_index in range(len(input_string)):

            current_char = input_string[char_index]

            if not freq_dict.get(input_string[char_index]):

                current_sequence += current_char
                freq_dict[current_char] = char_index


            else:

                potential_pal = input_string[freq_dict.get(current_char):char_index + 1]

                if len(potential_pal) > len(current_sequence):

                    if check_pal(potential_pal):
                        potential_candidates.append(potential_pal)
                        freq_dict[current_char] = char_index

                    else:

                        freq_dict[current_char] = char_index
                        current_sequence += current_char


                elif len(potential_pal) < len(current_sequence):

                    if check_pal(potential_pal):
                        potential_candidates.append(potential_pal)
                        current_sequence += current_char

                    else:

                        current_sequence = input_string[freq_dict.get(current_char) + 1:char_index + 1]
                        freq_dict[current_char] = char_index



                else:
                    if check_pal(potential_pal):

                        potential_candidates.append(potential_pal)


                    else:
                        current_sequence = input_string[freq_dict.get(current_char) + 1:char_index + 1]
                        freq_dict[current_char] = char_index
