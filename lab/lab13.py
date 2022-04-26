"""
1: Determine the Big-O notation
------------------------------------

The Big O notation for f(n) can be derived from the following simplification rules:

    - If f(n) is a sum of several terms, we keep only the one with largest growth rate.
        In order best to worst Big-O complexity: 1 < log n < n < n log n < n^2 < 2^n < n!
    - If f(n) is a product of several factors, any constant is omitted.

A) f(n) = O(n^2 + 3n + 6 + 3*2^n)

As the input n gets large, the behavior of the function is dominated by the term with the fastest growth
From rule 1, the term in f(n) with the largest growth rate is the dominant term 3*2^n
from rule 2, 3 is a constant in 3*2^n because it does not depend on n, so it is omitted.
Here our runtime is 2^n, and the growth curve is exponential

B) f(n) = O((n + 5) * (n + 20))
Here our runtime is O(n*n), which is equal to n^2. The growth curve is in quadratic time


"""


# C. is value an even number
def is_even(value):
    if value % 2 == 0:
        return True
    else:
        return False


print(f'is 2 a even number: {is_even(2)}')
print(f'is 5 a even number: {is_even(5)}')

"""
C) Answer: O(1)
The function is_even has a constant run time complexity.
The function only takes one value, there is nothing to loop through here. 
No matter the size of the value, even if it big, it is simply divided by 2 to see if it is a integer or float.  
"""


# D. create pairs/combinations from list input
def create_pairs(char_list):
    number_pairs = []
    list_length = len(char_list)
    for i in range(list_length):
        for j in range(list_length):
            number_pairs.append((char_list[i], char_list[j]))
    return number_pairs


character_list = ['a', 'b', 'c', 1, 2, 3]
print(create_pairs(character_list))

"""
D) Answer: O(n^2)
The function create_pairs has quadratic run time complexity. 
The first loop had O(n) complexity, and as the input length increases so will the times you run through the loop.
The inner loop also has O(n) complexity, but combined they have a quadratic run time complexity. 
"""


# E. double the value of all items in list
def double_list_values(number_list):
    list_length = len(number_list)
    if list_length == 0:
        return f'This list is empty, values cannot be doubled!'
    for index in range(list_length):
        number_list[index] *= 2
    return number_list


numbers_list = [2, 6, 1, 5, 20, 50]
print(double_list_values(numbers_list))

"""
E) Answer: O(n)
The function double_list_values had linear run time complexity. 
As number_lists length increases the number of iterations needed increases at the same rate. 
"""

"""
2: Proving Big-O 
------------------------------------
Determine a constant c>0 such that: T(n) < c.𝑓(n) 

A) Show that T(n) = 6n + 4 is O(n)		

Choose n0 = 1
assuming n > 1, then let us take a look at the condition:

6n + 4 ≤ c.n then (6+4)n ≤ c

Choose C = 10 (= 6+4) for n ≥ n0 = 1

Thus 6n + 4 is O(n) because 6n + 4 ≤ 10n whenever n > 1. 




B) Show that T(n) = n^2 + 5n + 2 is O(n^2)		

Choose n0 = 1
assuming n > 1, then let us take a look at the condition:

n^2 + 5n + 2 ≤ c.n^2 then (1+5+2)n^2 ≤ c

Choose C = 8 (= 1+5+2) for n ≥ n0 = 1

Thus n^2 + 5n + 2 is O(n^2) because n^2 + 5n + 2 ≤ 8n^2 whenever n > 1. 



"""

# TASK LIST,
"""
Joey have gotten in some trouble and have two lists of twitter ids that were supposed to match but they seem to not match
how can Joey check if they match if he assumes they are the same, when he expects one might be longer than the other?
Help Joey with this problem, bonus points for the efficency of your algorithm


Normaly these ids would be much longer, but as I could not find the ones I used when i did this and to spare you some
time these will do, besides it is the theory thats important
"""
a = [9, 8, 7, 6, 5, 4, 3, 2, 1]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 22]


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
b1 = quick_sort(b)

print("a1: ", a1)
print("b1: ", b1)
if a1 == b1:
    print('they are the same items')
else:
    print('they are not the same items')

b1.pop(-1)
print("fixed b:", b1)
if a1 == b1:
    print('they are the same items')
else:
    print('they are not the same items')

# Here we use Quick sort to see if the list are equal, if these had been bigger then this would still be fine but
# Issues may have arosen if they were different say on spot 550 - 560, then a more thorugh soloution had to be implemented
# Can you think on how you would solve it then?
# hint: For loops may be of use as you have to go through each element in the lists and see if they are equal

# Lists are ordered. Another way to check if list a and b are equal without sorting them is converting them to sets (sets are unordered) and 
# using set metods such as intersection and differnce (think about venn diagrams and how one can see what items are the same or differnt when comparing two sets) 

al = [9, 8, 7, 6, 5, 4, 3, 2, 1]

bl = [1, 2, 3, 4, 5, 6, 7, 8, 9, 22]

list1_as_set = set(al)
list2_as_set = set(bl)

intersection = list1_as_set.intersection(list2_as_set)
print(intersection)
if list1_as_set == list2_as_set == intersection:
    print('they are the same items')
else:
    print('they are not the same')

print(list1_as_set.difference(list2_as_set))
print(list2_as_set.difference(list1_as_set))
