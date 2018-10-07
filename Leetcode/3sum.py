"""
This file contains the class
to implement 3 sum problem
"""


class ThreeSum:
    """

    The class contains a method to implement the 3sum problem
    """

    def three_sum(self, input_array):

        input_array.sort()

        seen_set = set()

        for index1 in range(len(input_array) - 2):

            num1 = input_array[index1]
            twosum_target = -num1

            index_left = index1 + 1
            index_right = len(input_array) - 1

            while index_left < index_right:

                if input_array[index_left] + input_array[index_right] < twosum_target:

                    index_left += 1

                elif input_array[index_left] + input_array[index_right] > twosum_target:

                    index_right -= 1

                else:
                    if tuple(sorted([num1, input_array[index_left], input_array[index_right]])) not in seen_set:
                        seen_set.add(tuple(sorted([num1, input_array[index_left], input_array[index_right]])))
                        break

        return list(list(tup) for tup in seen_set)


sol = ThreeSum()
print(sol.three_sum([0, 0, 0, 0]))

sol = ThreeSum()
print(sol.three_sum([-1, 0, 1, 2, -1, -4]))
