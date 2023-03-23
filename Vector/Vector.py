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

import Array

class Vector():
    """! Vector Class """
    def __init__(self):
        """Creates a new empty vector with an initial capacity
            of 2 elements. 
        """
        self._items = Array(2)
        self._numItems = 0
    
    def __len__(self):
        """Returns the number of items contained in the vector"""
        return self._numItems
    
    def contains(self, item):
        """Determines if the given item is contained in the vector

        Args:
            item (Any): item to check
        """
        for i in self:
            if i is item:
                return True
        
        return False

    def __getitem__(self, ndx):
        """Returns the item stored in the ndx element of the list.
        The value of ndx must be within the valid range.

        Args:
            ndx (int): vector index
        """
        assert ndx >= 0 and ndx < self._numItems, "Vector index out of range."
        assert type(ndx) is int, 'Index must be an int.'
        return self._items[ndx]

    def __setitem__(self, ndx, item):
        """Sets the element at position ndx to contain the given item.
        The value of ndx must be within the valid range.

        Args:
            ndx (int): vector index
            item (Any): value to be set
        """
        assert ndx >= 0 and ndx < self._numItems, "Vector index out of range."
        assert type(ndx) is int, 'Index must be an int.'
        self._items[ndx] = item

    def append(self, item):
        """Adds the given item to the end of the list. 

        Args:
            item (Any): Item to be appended
        """
        if self._numItems < len(self._items):
            self._items[self._numItems] = item
        else:
            self._doubleSize()                        
            self._items[self._numItems] = item
        
        self._numItems += 1

    def insert(self, ndx, item):
        """Intesrts the given item in the element at position ndx.

        Args:
            ndx (int): Vector index
            item (Any): Item to be assigned
        """
        assert ndx >= 0 and ndx < self._numItems, "Vector index out of range."
        assert type(ndx) is int, 'Index must be an int.'

        self._shiftRight(ndx)
        self._items[ndx] = item
        self._numItems += 1

    def remove(self, ndx):
        """Removes and returns the item from the element from the given ndx position.

        Args:
            ndx (int): Item index to be removed

        Returns:
            Any: Removed item.
        """
        assert ndx >= 0 and ndx < self._numItems, "Vector index out of range."
        assert type(ndx) is int, 'Index must be an int.'

        retItem = self._items[ndx]

        self._shift(ndx, -1)
        self._numItems -= 1

        return retItem

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
        return _VectorIterator( self )
    

    def _doubleSize(self):
        new_arr = Array( len(self._items)*2 )
            
        for i in range(self._numItems):
            new_arr[i] = self._items[i]
        
        self._items = new_arr

    def _shift(self, position, numElements = 1):
        """Shifts the underlying array from position numElements elements.
        If numElements is a positive value, it shifts the array right.
        Shifting right it assumes the numElements is less than the doubled 
        size of the array. When numElements is a negative value is shifts
        the array left. It cannot shift beyonds zero index.
        
        Args:
            position (int): index from which to shift right
            elements (int): number of elements to shift
        """
        if numElements > 0:
            if numElements + self._numItems < len(self._items):
                for i in range(self._numItems - 1, self._numItems - position, -1):
                    self._items[i + numElements] = self._items[i]
            else:
                self._doubleSize()
                for i in range(self._numItems - 1, self._numItems - position, -1):
                    self._items[i + numElements] = self._items[i]
        else:
            assert self._numItems - position >= abs(numElements), 'Cannot shift left beyond index 0.'
            
            for i in range(position, self._numItems, 1):
                    self._items[i + numElements] = self._items[i]


class _VectorIterator():
    def __init__(self, vector):
        self._vector = vector
        self._curNdx = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._curNdx < len(self._vector):
            item = self._vector[self._curNdx]
            self._curNdx += 1
            return item
        else:
            raise StopIteration

v = Vector()