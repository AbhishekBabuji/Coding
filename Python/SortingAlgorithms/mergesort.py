"""This is a script that
has a function that performs merge sort

"""

def merge_sort(inputlist):

    """Sorts a list inplace.

    Args:
        inputlist (list): The first parameter

    Returns:
        None

    """

    if len(inputlist) > 1:
        mid = len(inputlist) // 2
        lefthalf = inputlist[:mid]
        righthalf = inputlist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        lefthalf_index = 0
        righthalf_index = 0
        mainlist_index = 0
        while lefthalf_index < len(lefthalf) and righthalf_index < len(righthalf):
            if lefthalf[lefthalf_index] < righthalf[righthalf_index]:
                inputlist[mainlist_index] = lefthalf[lefthalf_index]
                lefthalf_index = lefthalf_index + 1
            else:
                inputlist[mainlist_index] = righthalf[righthalf_index]
                righthalf_index = righthalf_index + 1
            mainlist_index = mainlist_index + 1

        while lefthalf_index < len(lefthalf):
            inputlist[mainlist_index] = lefthalf[lefthalf_index]
            lefthalf_index = lefthalf_index + 1
            mainlist_index = mainlist_index + 1

        while righthalf_index < len(righthalf):
            inputlist[mainlist_index] = righthalf[righthalf_index]
            righthalf_index = righthalf_index + 1
            mainlist_index = mainlist_index + 1
    #print("Merging ", inputlist)


if __name__ == '__main__':

    inputlist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    merge_sort(inputlist)
    print(inputlist)
