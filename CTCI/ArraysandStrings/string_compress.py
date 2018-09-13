"""Implement a method to perform basic string compression
using the counts of repeated characters. For example,
the string 'aabcccccaaa' would become a2b1c5a3. If
the compressed string would not become smaller than the
original string, your method should return the original
string.


"""


class Solution:
    """
    A class that contains an instance method to implement
    the above algorithm.

    """

    def string_compress(self, inputstring):

        """


        Args:
            inputstring (str): Uncompressed string

        Returns:
            compressed_string (str): Compressed inputstring or original inputstring depending
            on the length

        """

        compressed_string: str = ''

        samechar_count = 1

        if len(inputstring) > 1:

            for char_index in range(1, len(inputstring)):

                char_now = inputstring[char_index]
                char_prev = inputstring[char_index - 1]

                if char_prev == char_now:
                    samechar_count += 1

                else:

                    compressed_string = compressed_string + char_prev + str(samechar_count)
                    samechar_count = 1

            if char_index == len(inputstring) - 1:
                compressed_string = compressed_string + char_now + str(samechar_count)

        return compressed_string


example = Solution()
print(example.string_compress('tTTttaAbBBBccDd'))
