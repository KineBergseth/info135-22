"""Hashing is a technique of mapping a large set of arbitrary data to tabular indexes using a hash function. It is a
method for representing dictionaries for large datasets. After storing a large amount of data, we need to perform
various operations on these data. Lookups are inevitable for the datasets. Linear search and binary search perform
lookups/search with time complexity of O(n) and O(log n) respectively. As the size of the dataset increases,
these complexities also become significantly high which is not acceptable.

We need a technique that does not depend on the size of data. Hashing allows lookups, updating and retrieval
operation to occur in a constant time i.e. O(1).

The Hash table data structure stores elements in key-value pairs where

    Key- unique integer that is used for indexing the values
    Value - data that are associated with keys.

In a hash table, a new index is processed using the keys. And, the element corresponding to that key is stored in the
index. This process is called hashing.

Let k be a key and h(x) be a hash function. h(k) will give us a new index to store the element linked with k.


Hash Collision
When the hash function generates the same index for multiple keys, there will be a conflict (what value to be stored in
that index). This is called a hash collision.
We can resolve the hash collision using one of the following techniques.

    -Collision resolution by chaining:
        In chaining, if a hash function produces the same index for multiple elements,
        these elements are stored in the same index by using a doubly-linked list.
    -Open Addressing: Linear/Quadratic Probing and Double Hashing:
        Unlike chaining, open addressing doesn't store multiple elements into the same slot. Here, each slot is either
        filled with a single key or left NIL.
        -In linear probing, collision is resolved by checking the next slot.
        -quadratic probing is similar to linear, but the spacing between the slots is increased (greater than one)
        -in double hashing if a collision occurs after applying a hash function h(k),
            then another hash function is calculated for finding the next slot.


Applications of Hash Table - Hash tables are implemented where:

    constant time lookup and insertion is required
    cryptographic applications
    indexing data is required

"""

# HashTable example

hashTable = [[], ] * 11  # create hashtable with 11 spaces


def hashFunction(key):  # hash function to find index for hashtable
    """
    A simple hash function with remainder, where the element is divided by the table size.
    The result is the elements' table slot (index)
    """
    return key % len(hashTable)


def insertData(key, data):  # function to insert data
    """
    When we want to insert data, we first calculate the slot we want to insert the key/value pair in
    with a hash function, then we insert the data.
    """
    index = hashFunction(key)  # call on hashfunction to create an index
    hashTable[index] = [key, data]  # insert key and value with the index we found


def removeData(key):
    """
    To remove data we must first find the slot it is stored it. To do that we use the same method
    as when we inserted the data. We use the key to calculate the slot it is located in.
    """
    index = hashFunction(key)  # find index for item to remove with hash function
    hashTable[index] = []  # replace values with empty list on given index


# insert data to table, with a unique key and a belonging value
insertData(123, "banana")
insertData(284, "apple")
insertData(271, "pear")
insertData(132, "mango")

print(hashTable)

removeData(123)  # remove bananas from the table

print(hashTable)  # print updated table
