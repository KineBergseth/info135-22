"""
INFO135 - Lab 3 suggested solutions
Note that this is simply a suggestion of how to solve the tasks, there will be many other valid
solutions. :D

"""
from typing import List, Tuple
from typing import Tuple

"""
Exercise 1

Write a function that performs exactly one pass of selection sort on any given list of integers.

Example:
selection_sort_one_pass([5, 2, 3, 4, 0, 1])
>> > [0, 2, 3, 4, 5, 1]

 """

unsorted_list: List[int] = [5, 2, 3, 4, 0, 1]


def one_pass(li: List[int], index: int) -> List[int]:
    """
    The first item in an unsorted partition is compared with all the values to the right-hand side to check if it is
    the minimum value. If it is not the minimum value, then its position is swapped with the minimum value.
    :param li: an unsorted list containing integers
    :param index: Indicate the left most item (first position) in the unsorted partition by index
    :return: list containing integers, with one sorted pass performed
    """
    # Create sublist from first position, where the leftmost value (index) is the start of the partition
    sub_list = li[index:]
    # Find the minimum element in the unsorted subarray
    smallest = min(sub_list)
    # Find the index of the minimum element on the right-hand side of first position
    # sub_list.index(smallest) excludes values not in sub_list, does not start at index 0 of li
    # to find real index in li (argument), we make up for potential items on the left side of sub_list hence + index
    smallest_index = sub_list.index(smallest) + index

    # Swap the found minimum element with the first element
    # The first position takes the position previously held by the lower value, and
    # The lower value from the right-hand side takes the first position
    li[index], li[smallest_index] = li[smallest_index], li[index]

    """
    # Python allows us to switch the elements with a = b, b = a in one line as seen on the line above ^
    # Another way to switch the values is to hold them in temp variable like so:
    # The leftmost value (index) is stored in a temporal variable
    temp = li[index]
    li[index] = li[smallest_index]
    li[smallest_index] = temp
    """

    return li


def one_pass_0(li: List[int]) -> List[int]:
    smallest = min(li)

    smallest_index = li.index(smallest)

    li[0], li[smallest_index] = li[smallest_index], li[0]

    return li


print(f"One pass result: {one_pass_0(unsorted_list)}")
print(f"Unsorted list: {unsorted_list}")
print(f"One pass result: {one_pass(unsorted_list, 0)}")
print()  # Create empty line before next print to separate exercises prints

"""
Exercise 2 

File large_list.py contains a list of 104.6 tuples each containing 3 numbers. Write an algorithm that iterates 
through each tuple and creates a new list containing each tuple where the sum of index 0 and 1 equal index 2. 

Sort the new list containing only valid tuples so that the last elements of the tuples are in ascending order.  
Use a sorting algorithm of your choice. 

Example: 

>>> tuples = [(0,0,1), (0,1,1), (0,1,2), (1,1,2), (1,2,3)] 
>>> tuples = filter_tuples(tuples) 
>>> selection_sort(tuples) 
> [(0,1,1), (1,1,2), (1,2,3)] 
"""
# Import variable 'liste' from the file large_list.py
from large_list import liste


def filter_tuples(t_list: List[Tuple[int, int, int]]) -> List[Tuple[int, int, int]]:
    """
    Function that iterates through each tuple in a list and creates a new list containing each tuple where the sum of
    index 0 and 1 equal index 2
    :param t_list: a list consisting of tuples with 3 int values
    :return: a list consisting of tuples with 3 int values
    """
    tuple_list = []
    for tup in t_list:
        if tup[0] + tup[1] == tup[2]:
            tuple_list.append(tuple(tup))
    return tuple_list


def alternative_filter(t_list: List[Tuple[int, int, int]]) -> List[Tuple[int, int, int]]:
    """
    Function that iterates through each tuple in a list and creates a new list containing each tuple where the sum of
    index 0 and 1 equal index 2
    :param t_list: a list consisting of tuples with 3 int values
    :return: a list consisting of tuples with 3 int values
    """
    tuple_list = [tup for tup in t_list if tup[0] + tup[1] == tup[2]]
    return tuple_list


def selection_sort(t_list: List[Tuple[int, int, int]]) -> None:
    """
    A selection sort algorithm, sorts a list of tuples so that the last elements of the tuples are in ascending order
    :param t_list: a list consisting of tuples with 3 int values
    """
    # sort by third element of tuple, set nth to be 2
    nth = 2
    for index in range(len(t_list)):

        # Set index to be the minimum element in the unsorted list
        smallest_index = index
        #  Compare the leftmost value to the other values on the right-hand side
        # J does not start at 0, but at 'index + 1', this excludes values that have been sorted
        for j in range(index + 1, len(t_list)):
            # Finds the minimum value in the unsorted list and places it in its proper position
            # [nth] sort by the nth element of tuple
            if t_list[smallest_index][nth] > t_list[j][nth]:
                # Update smallest value if the condition is true
                smallest_index = j

        # Swap the found minimum element with the first element
        t_list[index], t_list[smallest_index] = t_list[smallest_index], t_list[index]


tuples = filter_tuples(liste)
selection_sort(tuples)
print(tuples)

"""
Exercise 3

Write a function that can take in two strings as function arguments and determine if they are anagrams or not, 
and print the result in the console. An anagram is a word or phrase formed by rearranging the letters of a different 
word or phrase. Two words are anagrams of each other if they contain the same number of characters and the same 
amount of each character. 

Examples of anagrams are as follows: abc = cba, ABBA = baba, Cat = Act, 
Astronomer = Moon starer, The Detectives = Detect Thieves, Funeral = Real fun, Listen = Silent. 

You need to sort the characters in lexicographic order (alphabetical order), and determine if all the characters in 
one string are equal to and in the same order as all the characters in the other string. To allow for strings with 
upper case letters and phrases with spaces, you should convert the string values into lowercase and remove spaces 
before you sort the characters. 

You are not allowed to do this the easy way and use inbuilt functions such as the sorted() function, you must utilize 
another sorting algorithm of your choice (Like bubble sort, selection sort, insertion sort etc). 
"""


def bubble_sort(str_list: List[str]) -> None:
    """
    A bubble sort algorithm, that sorts a list of string values in lexicographic order (alphabetical order).
    :param str_list: List: a list of string values that is to be sorted
    """
    # Assign length of the list to variable
    list_length = len(str_list)

    # Traverse through all list elements starting from 0, stopping before last element. We could use only list_length,
    # but outer loop will repeat one time more than needed since second to last item will compare to last item, hence -1
    for i in range(list_length - 1):

        # Inner loop that compares all the values in the list from the first to the last one
        for j in range(0, list_length - 1):
            # Check if the value on the left-hand side is greater than the one on the immediate right side
            if str_list[j] > str_list[j + 1]:
                # Swap elements if the element found is greater than the next element
                str_list[j], str_list[j + 1] = str_list[j + 1], str_list[j]


def anagram_checker(s1: str, s2: str) -> None:
    """
    A function that checks if two string values are anagrams of each other
    :param s1: a string value
    :param s2: a string value
    """
    string1, string2 = clean_strings(s1, s2)

    if len(string1) != len(string2):
        print("The strings are not the same length, therefore they are not anagrams")
    else:
        bubble_sort(string1)
        bubble_sort(string2)
        # Check if the two strings are equal/identical and match character by character
        if string1 == string2:
            print(f"The strings '{s1}' and '{s2}' are anagrams")
        else:
            print(f"The strings '{s1}' and '{s2}' NOT anagrams")


def clean_strings(s1: str, s2: str) -> Tuple[List[str], List[str]]:
    """
       Processes two string values. Removes spaces, converts values to all lowercase and convert them to lists
       :param s1: a string value
       :param s2: a string value
       :return: returns a tuple containing the processed string1 and string2 values in list form
       """
    string1 = s1.replace(" ", "").lower()
    string2 = s2.replace(" ", "").lower()
    string1, string2 = list(string1), list(string2)
    return string1, string2


# a list of string that may or may not be anagrams
potential_anagrams: List[Tuple[str, str]] = [('abc', 'cda'), ('ABBA', 'baba'), ('Cat', 'adt'),
                                             ('The Detectives', 'Detect Thieves'), ('Listten', 'Silent')]

print()  # make empty line to separate from last print
# for each tuple in the list potential_anagrams, check if the pair is an anagram
for string in potential_anagrams:
    anagram_checker(string[0], string[1])
