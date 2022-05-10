a = [5, 4, 8, 7, 5, 1, 3, 0]
b = [5, 4, 8, 7, 5, 1, 3, 0]
c = [5, 4, 8, 7, 5, 1, 3, 0]
d = [5, 4, 8, 7, 5, 1, 3, 0]
e = [5, 4, 8, 7, 5, 1, 3, 0]

"""
QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways. 

    Always pick first element as pivot.
    Always pick last element as pivot (implemented below)
    Pick a random element as pivot.
    Pick median as pivot.

The key process in quickSort is partition(). Target of partitions is, given an array and an element x of array as pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. 
"""
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        # here we pick the first element, prob better picking a different one
        # Make rather partion function
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)


a1 = quick_sort(a)
print("quick: ", a1)

"""
The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.
1) The subarray which is already sorted. 
2) Remaining subarray which is unsorted.
In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.
"""
def selection_sort(t_list):
    """
    A selection sort algorithm, sorts a list in ascending order
    """
    for index in range(len(t_list)):

        # Set index to be the minimum element in the unsorted list
        smallest_index = index
        #  Compare the leftmost value to the other values on the right-hand side
        # J does not start at 0, but at 'index + 1', this excludes values that have been sorted
        for j in range(index + 1, len(t_list)):
            # Finds the minimum value in the unsorted list and places it in its proper position
            if t_list[smallest_index] > t_list[j]:
                # Update smallest value if the condition is true
                smallest_index = j

        # Swap the found minimum element with the first element
        t_list[index], t_list[smallest_index] = t_list[smallest_index], t_list[index]


selection_sort(b)
print("selection: ", b)

"""
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order.
"""
def bubble_sort(li) -> None:
    """
    A bubble sort algorithm, that sorts a list of values
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


bubble_sort(c)
print("bubble: ", c)

"""
Insertion Sort Algorithm 
To sort an array of size n in ascending order: 
1: Iterate from arr[1] to arr[n] over the array. 
2: Compare the current element (key) to its predecessor. 
3: If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.
"""


def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


insertion_sort(d)
print("insert: ", d)


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
"""
def mergeSort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
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


#http://web.mit.edu/16.070/www/lecture/big_o.pdf
