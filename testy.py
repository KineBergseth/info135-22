def selection_sort(t_list) -> None:
    """
    A selection sort algorithm, sorts a list of tuples so that the last elements of the tuples are in ascending order
    :param t_list: a list consisting of tuples with 3 int values
    """
    # sort by third element of tuple, set nth to be 2
    # Traverse through all tuples in list
    for index in range(len(t_list)):

        # Set index to be the minimum element in the unsorted list
        smallest_index = index
        #  Compare the leftmost value to the other values on the right-hand side
        # J does not start at 0, but at 'index + 1', this excludes values that have been sorted
        for j in range(index + 1, len(t_list)):
            # Finds the minimum value in the unsorted list and places it in its proper position
            # [nth] sort by the nth element of tuple
            if t_list[smallest_index]> t_list[j]:
                # Update smallest value if the condition is true
                smallest_index = j

        # Swap the found minimum element with the first element
        t_list[index], t_list[smallest_index] = t_list[smallest_index], t_list[index]


def s(arr):
    new_list = []
    for num in arr:
        if num not in new_list:
            new_list.append(num)
    selection_sort(new_list)
    return new_list


ny_list = [1, 2, 5, 2, 1, 0, 7, 2, -3]
ss = s(ny_list)
print(ss)
