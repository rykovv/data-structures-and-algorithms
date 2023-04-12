##
# @file LinkedList.py
# 
# @brief Implementation of Unordered LinkedList data structure and its test
#
# @section description_linkedlist Description
# Implementation of Unordered LinkedList data structure and its test
# 
# @section notes_linkedlist Notes
# - 
# 
# @section todo_linkedlist TODO
# -
#
# @section author_linkedlist Author
# - Vladislav Rykov
#
##

class Node():
    data = None
    nextNode = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return self.data

class LinkedList():
    """! Unordered LinkedList base class """

    def __init__(self):
        self._nodes = None
        self._count = 0

    def add(self, data):
        node = Node(data)
        node.nextNode = self._nodes
        self._nodes = node
        self._count += 1

    def remove(self, data):
        if data in self:
            prevNode = None
            for node in self:
                if node.data == data:
                    if prevNode is None:
                        self._nodes = node.nextNode
                    else:
                        prevNode.nextNode = node.nextNode
                else:
                    prevNode = node
                

    def __contains__(self, data):
        for node in self:
            if node.data is data:
                return True
        return False

    def __iter__(self):
        return _LinkedListIterator(self)

    def __len__(self):
        return self._count

class _LinkedListIterator():
    def __init__(self, theList):
        self._curNode = theList

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._curNode is not None:
            curNode = self._curNode
            self._curNode = self._curNode.nextNode
            return curNode
        else:
            raise StopIteration