"""
Excercise 1

The First one, is a joke for one of the most horrible "trees" you can have, it is truly horrendous set up of a tree.(Yuck)
It is not perfect, complete, full or even binary it is truly awful

B is a full, complete, binary tree

C is full, perfect, complete binary tree.

"""




""""
Exercise 2

graph = [(“A”,“B”), (“A”,“C”), (“B”,“A”), (“C”,“A”), (“B”,“C”)] 

Given the Graph graph, make a function remove_node(node) which removes all edges connected to a given node. 
"""


class Graph:
    graph = dict()
    searched = []

    def add_edge(self, node, neighbour):
        if node not in self.graph:
            self.graph[node] = [neighbour]
        else:
            self.graph[node].append(neighbour)

    def print_graph(self):
        print(self.graph)

    def print_edges(self):
        for nodes in self.graph:
            for neighbour in self.graph[nodes]:
                print("(", nodes, ",", neighbour, ")")

    # Method that removes the given node and the edges
    # Sets nodes that are only connected to the node that is about to be deleted as []
    # Can you spot some not intended features or bugs?
    def delete_edges(self, node):
        del self.graph[node]
        for nodes in self.graph:
            p = len(self.graph[nodes])
            if self.graph[nodes][p-1] == node:
                del self.graph[nodes][p-1]



my_graph1 = Graph()
my_graph1.add_edge('1', '2')
my_graph1.add_edge('3', '2')
my_graph1.add_edge('2', '3')
my_graph1.add_edge('2', '4')
my_graph1.add_edge('1', '3')
my_graph1.add_edge('1','4')
my_graph1.add_edge('2','1')
my_graph1.add_edge('4','2')
my_graph1.add_edge('4','1')
my_graph1.add_edge('5','1')

print('before ')
my_graph1.print_graph()
my_graph1.delete_edges('1')
print('After ')
my_graph1.print_graph()

"""
You are faced with a security door with a super secret password that you want to hack.

The door has a four-character password that is generated one character at a time by
finding the MD5 hash of the door ID, and an increasing integer index that starts at 0. 
The value you need to hash is the string (doorID + index). E.g. 'abc0', 'abc1', 'abc2' etc 

A hash contains a digit of the password if the hash hexadecimal representation starts with two zeroes.
If it does contain two zeroes in the beginning, the fourth character in the string is part of the 4-digit password.

The door ID is: cyd

You will need to use the module hashlib, and the function md5, which you can import as following: 
from hashlib import md5

some functions you will need is:
md5(): generate a MD5 hash value from a String input
encode() : Converts the input string into bytes to be acceptable by hash function.
hexdigest() : Returns the encoded data in hexadecimal format.

To get the hexadecimal representation of a doorId + index:
The value you wish to hash must be encoded before hashing, and
you must use hexdigest() on the encoded data (the result from md5) to get it in hexadecimal format.

OBS: the index must be converted to a string value. 'abc'18 will not work, but 'abc18' will work in the hash function


For example, if the door ID is "abc":
The first index which produce a hash that starts with two zeroes is 19, which we find by hashing the string 'abc19'. 
The result is the hexadecimal representation 0034e0923cc38887a57bd7b1d4f953df, and the first character of the password
is the fourth character in the string, thus '4' is the first character in the password.

186 is the next index that produce a hash that begins with two zeroes (005fcb89...), giving us the character 'f'.
The next hashes that starts with two zeroes are index 445 (0066030a...) and index 616 (0074e164...), 
which gives us the characters '6' and '4'. After finding the four characters, we found that the password is '4f64'.

Given the actual Door ID 'cyd', what is the password to the door? 

"""

from hashlib import md5


# Finds the first four hashes that starts with 00 and finds a specific character of our password so we can hack door
def crack_door(door_code):
    password = []
    i = 0
    # While password is less than 4 characters, continue to search for the missing characters
    while len(password) < 4:
        # generate md5 hash of door_id + index
        h = md5((door_code + str(i)).encode()).hexdigest()
        # increase index so we can hash next number next time
        i = i + 1
        # If the hash value starts with two 00, is contains a character in the password
        if h[:2] == '00':  # h.startswith("00") also works here
            print(F"Hash function input '{door_code}{str(i)}', Hash result: {h}, Password character {h[3]}")
            # add password character to out password list
            password.append(h[3])
    # Print password
    print(f"The password to the door {door_code} is: ")
    print(*password)


door_id = "cyd"
crack_door(door_id)
