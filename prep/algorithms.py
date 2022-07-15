"""
Innholdsliste:

Bubble sort
Selection sort
Insertion sort
Quick sort
Merge sort


Greedy algorithms
Dynamic programming
"""

# eksempel lister for sortering
a = [5, 4, 8, 7, 6, 1, 3, 0]
b = [5, 4, 8, 7, 6, 1, 3, 0]
c = [5, 4, 8, 7, 6, 1, 3, 0]
d = [5, 4, 8, 7, 6, 1, 3, 0]
e = [5, 4, 8, 7, 6, 1, 3, 0]
print('original list:', a)


def bubble_sort(li):
    """
    Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in
    the wrong order.
    BIG O worst case: O(n^2)
    """

    # Assign length of the list to variable
    list_length = len(li)

    # Traverse through all list elements starting from 0, stopping before last element. We could use only list_length,
    # but outer loop will repeat one time more than needed since second to last item will compare to last item, hence -1
    for i in range(list_length - 1):

        # Inner loop that compares all the values in the list from the first to the last one
        for j in range(0, list_length - 1):
            # Check if the value on the left-hand side is greater than the one on the immediate right side
            if li[j] > li[j + 1]:
                # Swap elements if the element found is greater than the next element
                li[j], li[j + 1] = li[j + 1], li[j]


bubble_sort(a)
print("bubble: ", a)

"""
The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.
1) The subarray which is already sorted. 
2) Remaining subarray which is unsorted.
In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.
"""


def selection_sort(t_list):
    """
    A selection sort algorithm, selects the smallest element from an unsorted list in each iteration and places that
    element at the beginning of the unsorted list by swapping the current smallest and the first unsorted item places
    The algorithm maintains two subarrays in a given array. a sorted part, and the remaining elements in an unsorted subarray.
    BIG O worst case: O(n^2)
    """
    for index in range(len(t_list)):

        # Set first element to be the minimum element in the unsorted list
        smallest_index = index
        #  Compare the leftmost value to the other values on the right-hand side
        # J does not start at 0, but at 'index + 1', this excludes values that have been sorted
        for j in range(index + 1, len(t_list)):
            # Finds the minimum value in the unsorted list and places it in its proper position
            if t_list[smallest_index] > t_list[j]:
                # Update the smallest value if the condition is true
                smallest_index = j

        # Swap the found minimum element with the first unsorted element
        t_list[index], t_list[smallest_index] = t_list[smallest_index], t_list[index]


selection_sort(b)
print("selection: ", b)


def insertion_sort(arr):
    """
    A simple sorting algorithm that works the way we sort playing cards in our hands.
    We traverse through the list and place an unsorted element at its correct place in each iteration.
    To sort an array of size n in ascending order:
    1: Iterate from arr[1] to arr[n] over the array.
    2: Compare the current element (key) to its predecessor.
    3: If the key element is smaller than its predecessor, compare it to the elements before. then..
    3: Move the greater elements one position up to make space for the swapped element.
    4: Place the key behind the smaller value, or in front if no smaller values are found
    (For descending order, change key<arr[j] to key>arr[j] in the while loop)

    Big O worst case: O(n^2)
    """
    # Traverse through 1 to len(arr) since first item is assumed to be already sorted.
    for i in range(1, len(arr)):
        key = arr[i]  # current element
        j = i - 1  # last sorted items index
        # Compare key with each element on the left of it until an element smaller than it is found
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # move sorted element to the right by one
            j -= 1
        arr[j + 1] = key  # Place key behind the element just smaller than it


insertion_sort(c)
print("insert: ", c)

"""
QuickSort is a Divide and Conquer algorithm. It picks an element from the array as a pivot and partitions the 
given array around the picked pivot. The pivot can be the first, last, median, or a random element.  


The key process in quickSort is partition(). Target of a partitions is that the pivot element should be positioned in 
such a way that elements less than pivot are kept on the left side and elements greater than pivot are on the right 
side of the pivot. So elements smaller than the pivot is in a left subarray, and elements greater are in a  
right subarray (if ascending order).

The left and right subarrays are also divided using the same approach. This process continues 
until each subarray contains a single element. At this point, elements are already sorted. Finally, elements are 
combined to form a sorted array. 

BIG O worst case: O(n log(n))
"""


def quick_sort(arr):
    if len(arr) < 2:  # if array is empty or has length of 1, is it already sorted
        return arr
    else:
        pivot = arr[0]  # here we pick the first element as pivot value

        less = []  # subarray with smaller values than pivot
        greater = []  # subarray with larger values than pivot
        for i in arr[1:]:  # traverse all items except pivot (pivot is first elem, so start from element at index 1)
            if i <= pivot:
                less.append(i)
            if i > pivot:
                greater.append(i)
            # append item to correct subarray

        return quick_sort(less) + [pivot] + quick_sort(greater)  # recursively sort subarrays and return result


quick = quick_sort(d)
print("quick: ", quick)

"""
Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two 
halves, and then it merges the two sorted halves.

MergeSort(arr[], l,  r)
If r > l
     1. Find the middle point to divide the array into two halves:  
             middle m = l+ (r-l)/2
     2. Call mergeSort for first half:   
             Call mergeSort(arr, l, m)
     3. Call mergeSort for second half:
             Call mergeSort(arr, m+1, r)
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(arr, l, m, r)
             
BIG O worst case: O(n log(n))
"""


def mergeSort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements into a left and right sublist, representing elements before and after mid
        L = arr[:mid]
        R = arr[mid:]

        # Sorting the first and second half recursively
        mergeSort(L)
        mergeSort(R)

        """
        create 3 pointers: 
        i maintains current index of L, starting at 1
        j maintains current index of R, starting at 1
        k maintains the current index in the sublist
        """
        i = j = k = 0

        # Until we reach either end of either L or R, pick larger among elements L and R and place them in the
        # correct position
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # when we have run out of elements in L and R, checking if any element are left and put in list
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


mergeSort(e)
print("merge: ", e)

"""
Greedy algorithms: https://www.programiz.com/dsa/greedy-algorithm
A greedy algorithm is an approach for solving a problem by selecting the best option available 
at the moment. It doesn't care whether the current best result will bring the overall optimal result. 

The algorithm never reverses the earlier decision even if the choice is wrong. It works in a top-down approach.

This algorithm may not produce the best result for all the problems. It's because it always goes for the local best 
choice to produce the global best result. 

However, we can determine if the algorithm can be used with any problem if the problem has the following properties:

1. Greedy Choice Property

If an optimal solution to the problem can be found by choosing the best choice at each step without reconsidering the 
previous steps once chosen, the problem can be solved using a greedy approach. This property is called greedy choice 
property. 

2. Optimal Substructure

If the optimal overall solution to the problem corresponds to the optimal solution to its subproblems, 
then the problem can be solved using a greedy approach. This property is called optimal substructure. 

Advantages of Greedy Approach

    The algorithm is easier to describe.
    This algorithm can perform better than other algorithms (but, not in all cases).



Dynamic programming: https://www.programiz.com/dsa/dynamic-programming
Dynamic Programming is a technique in computer programming that helps to efficiently solve a 
class of problems that have overlapping subproblems and optimal substructure property. 

If any problem can be divided into subproblems, which in turn are divided into smaller subproblems, and if there are 
overlapping among these subproblems, then the solutions to these subproblems can be saved for future reference. In 
this way, efficiency of the CPU can be enhanced. This method of solving a solution is referred to as dynamic 
programming. 

Such problems involve repeatedly calculating the value of the same subproblems to find the optimum solution.
"""
