"""
BIG O

CONTENT
    1. Big O Notation
    2. Sequential Statements
    3. Conditional Statements
    4. Loop Statements
    5. Nested loops statements
    6. Function call statements
    7. Recursive Functions Statements
    8. Prove Big O

    https://www.bigocheatsheet.com/
    https://developerinsider.co/big-o-notation-explained-with-examples/

"""

# 1. Big O Notation
"""
Big-O notation is a metric used to find an algorithms complexity. Big-O notation signifies the 
relationship between the input to the algorithm, and the steps/operations required to execute the algorithm. 
Big O refers to the upper bound of time/space complexity of an algorithm, aka what is the worst runtime scenario. 

When we count the operations taken by algorithms, we don't really care about one-off operations (constants factors); 
we care about actions that are related to the size of the input, n. For a list, that's the number of elements; 
for a string, it can be the number of characters. All that matters is the dominant term (the highest power of n). 

The Big O notation for f(n) can be derived from the following simplification rules:
    - If f(n) is a sum of several terms, we keep only the one with largest growth rate.
        In order best to worst Big-O complexity: 1 < log n < n < n log n < n^2 < 2^n < n!
    - If f(n) is a product of several factors, any constant factors is omitted.


In order from smallest to largest complexity:
Constant Time: O(1)
Logarithmic Time: O(log n)
Linear Time: O(n)
Linearithmic Time: O(n log n)
Quadric Time: O(n^2)
Cubic TIme: O(n^3)
Plynomial TIme: O(n^k)
Exponential Time: O(b^n)
Factorial Time: O(n!)
"""

# 2. Sequential Statements

"""
Basic operations like assigning variables, printing, comparisons can be assumed to be constant time complexity O(1).
AS long as you have a fixed number of operations it will be constant time, regardless if there are 1 or 100 of these 
statements. In the examples below, each statement is a basic operation, and the value of the numbers

OBS! Pass på når det er funksjonskall et sted. Da må du gå inn i den funksjonen og se den sin kjøretid!   
"""
# examples:
print(1 * 3)


def math(x, b):
    value = x + b
    print(value)


math(2, 3)

# 3. Conditional Statements
# example 1
a = 5

if a <= 0:
    print('a har verdien 0 eller mindre')
elif a == 1:
    print('a har verdien 1')
elif a == 2:
    print('a har verdien 2')
elif a == 3:
    print('a har verdien 3')
elif a == 4:
    print('a har verdien 4')
else:
    print('a har verdien 5 eller høyere. ')
"""
The above code is constant
"""

# example 2:
li = [3, 5, 1]
if len(li) == 0:
    print('li empty')
else:
    li.sort()
    print('li', *li)
"""
What complexity is the code in example 2 here? It may look like it is constant but that is wrong. The if block is 
constant time, but when we get to the else block we have a function call sort(). We dont see the function here, but the 
built in function sort() has the complexity O(n log n), which makes the complexity to all this code O(n log n).
"""

# 4. Loops
print('loops')
"""
Linear O(n) — performance becomes less efficient as data grows.
In Linear, performance is dependent on the input size.
Liner search is O(n):
"""
liste = [1, 3, 5, 7, 9, 11]


def lin_search(val):
    for item in liste:
        if item == val:
            return 'item found'
    else:
        return 'item not found'


print(lin_search(4))
print(lin_search(5))

"""
Logarithmic O(log N) — narrows down the search by repeatedly halving the dataset until you find the target value.

Using binary search — which is a form of logarithmic algorithm, finds the median in the array and compares it to the 
target value. The algorithm will traverse either upwards or downwards depending on the target value being higher 
than, lower than or equal to the median. 

This means that when we have a list and we want to search for the value x, we compare it to the middle value,
and thereafter exclude parts of the list in our progress. Which means we have to do less operations over time. 

"""


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        # If the value we are searching for x is greater, ignore left half and search only in right half of list
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half and search for x in left half
        elif arr[mid] > x:
            high = mid - 1

        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present in the list
    return -1


result = binary_search(liste, 3)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")


# 5. Nested loops
"""
Sometimes you might need to visit all the elements on a 2D array (grid/table). 
For such cases, you might find yourself with two nested loops.
 
In the example below we have two for loops:
"""
lis = [1, 2, 3]  # O(1)
print('nested loops pairs')  # O(1)
for n in lis:  # O(n)
    print('n is now ', n)  # O(1)
    for m in lis:  # O(n)
        print(n, m)  # O(1)

"""
Our outer loop runs n times, and our inner loop runs n times for each iteration of the outer loop.
The complexity here is something like: T(n) = n * [t(statement1) + n * t(statement2...3)]
Looking past the constant statements, we have a runtime of O(n * n), which is O(n^2)
"""

# 6. Function calls
"""
If the code makes a function call, you must be aware of its runtime. Lets say you have the following code:
"""
print('function calls')
v = [3, 2, 1]


def print_sequence(x):
    for number in x:
        print(number, end=" ")


if len(v) == 0:
    print('listen v er tom')
else:
    print_sequence(v)

"""
If we were to check out the following and determine the complexity, it looks like it is just constant operations:
if len(v) == 0:
    print('listen v er tom')
else:
    print_sequence(v)
    
which complexity does it have? 
The else statement has a function call to print_sequence() which is function with a loop with a linear complexity O(n).
So the code has the complexity O(n). 
"""

# 7. Recursive Functions
"""
Analyzing the runtime of recursive functions might get a little tricky. There are different ways to do it. 
One intuitive way is to explore the recursion tree. One typical example is fibonacci as seen below, where for each 
increase in length to the input, we must calculate the two previous numbers and add them together. 

    When you n = 2, you have 3 function calls. First fn(2) which in turn calls fn(1) and fn(0).
    For n = 3, you have 5 function calls. First fn(3), which in turn calls fn(2) and fn(1) and so on.
    For n = 4, you have 9 function calls. First fn(4), which in turn calls fn(3) and fn(2) and so on.

Since it’s a binary tree, we can sense that every time n increases by one, we would have to perform at most the double 
of operations. O(2^n) is a algorithm whose growth doubles with each addition to the input data set. 
"""
print('\nfibonacci')


def fibonacci(num):
    if num <= 1:
        return num
    return fibonacci(num - 2) + fibonacci(num - 1)


length = 5
for n in range(length):
    print(fibonacci(n), end=" , ")

# 8. Prove Big O
"""
les om det forelesning, på løsningsforslaget til lab 13 og div ressurser under. evt google "Prove big  O for video og guides"
https://www.youtube.com/watch?v=NBwxUHQlLhs
https://www.youtube.com/watch?v=8oAaivb40Ds

https://developerinsider.co/big-o-notation-explained-with-examples/ <- se nederst
http://web.mit.edu/16.070/www/lecture/big_o.pdf
https://mfleck.cs.illinois.edu/building-blocks/version-1.2/big-o.pdf
"""
