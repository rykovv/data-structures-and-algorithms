##
# @file Vector.py
# 
# @brief Implementation of Vector based on Array Python
#   native data structure and its test
#
# @section description_vector Description
# Implementation of Vector based on Array Python
#   native data structure and its test
# 
# @section notes_vector Notes
# - 
# 
# @section todo_vector TODO
# -
#
# @section author_vector Author
# - Vladislav Rykov
#
##

from array import array

class Vector():
    """! Vector Class """
    def __init__(self):
        """Creates a new empty vector with an initial capacity
            of 2 elements. 
        """
        self._items = array('l', 2)
    
    def __len__(self):
        """Returns the number of items contained in the vector"""
        return len(self._items)
    
    def contains(self, item):
        """Determines if the given item is contained in the vector

        Args:
            item (Any): item to check
        """
        # TODO
        pass

    def getitem(self, ndx):
        """Returns the item stored in the ndx element of the list.
        The value of ndx must be within the valid range.

        Args:
            ndx (int): vector index
        """
        # TODO
        pass

    def setitem(self, ndx, item):
        # TODO
        pass

    def append(self, item):
        # TODO
        pass

    def insert(self, ndx, item):
        # TODO
        pass

    def remove(self, ndx):
        # TODO
        pass

    def indexOf(self, item):
        # TODO
        pass

    def extend(self, otherVector):
        # TODO
        pass

    def subVector(self, ndx_from, ndx_to):
        # TODO
        pass

    def __iter__(self):
        # TODO
        pass

v = Vector()