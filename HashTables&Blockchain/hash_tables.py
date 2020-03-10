# add node class to implement linked list chaining within hash table

class Node:
    def __init__(self, key, value):
    self.key = key 
    self.value = value 
    self.next = None 

class HashTable:
    def __init__(self, capacity, buckets):    
        # no of storage buckets hash table can hold
        self.capacity = capacity 
        # initialise storage to be an array of Nones * capacity
        self.buckets = [None] * capacity

    # Take an arbitrary key and return a valid integer index
    # within the storage capacity of the hash table.
    def _hash(self, key):
        return hash(key) % self.capacity

    # insert key value pair into hash table, handling collisions by using linked list chaining
    def insert(self, key, value):
        # generate the index at which we'll hold the Node
        index = self._hash(key)
        # check if any other node already resides at given index
        if self.buckets[index] is None:
            # if so, no collision has occurred -> add new Node and return from function
            self.buckets[index] = Node(key, value)    
            return
        # else, collision has occurred and one or more nodes reside at given index -> iterate over the list while node is not None
        # store the value of the previous node in list in 'prev' variable 
        node = self.buckets[index]
        prev = node
        while node is not None:
            # check if the key already exists in one of the nodes while iterating, 
            if prev.key == key: 
                # if so just overwrite the value 
                prev.value = value
            # else continue iterating the end    
            # set the value of the prev node equal to the current node
            prev = node
            # set the vaue  of the current node equal to the next node
            node = node.next
        # when we're finished iterating over the list (node is equal to none and we've exited while loop),
        # add new node
        prev.next = Node(key, value)    