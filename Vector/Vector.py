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

from Array import Array

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
            self._increaseSizeBy(2)
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

        self._shift(ndx)
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

        if self._numItems <= len(self._items)/3:
            self._decreaseSizeBy(2)

        return retItem

    def indexOf(self, item):
        """Returns the index of the vector element containing the given item.
        The item must be in the list.

        Args:
            item (Any): Item to be searched for

        Returns:
            int: item's index in the Vector
        """
        for ndx, itm in enumerate(self):
            if itm is item:
                return ndx

    def extend(self, otherVector):
        """Extends this vector by appending the entire contents of the otherVector
        to this vector

        Args:
            otherVector (Vector): Vector to be appended
        """
        for i in otherVector:
            self.append(i)

    def subVector(self, ndx_from, ndx_to):
        """Creates and returns a new Vector that contains a subsequence of the items
        in the vector between and including those indicated by the given ndx_from and
        ndx_to.

        Args:
            ndx_from (int): from index
            ndx_to (int): to index
        """
        assert  ndx_from < ndx_to and                               \
                (ndx_from >= 0 and ndx_from < self._numItems) and   \
                (ndx_to >= 0 and ndx_to < self._numItems), 'Incoherent indices.'
        
        subv = Vector()
        for i in range(ndx_from, ndx_to, 1):
            subv.append(self._items[i])

        return subv

    def __iter__(self):
        return _VectorIterator( self )
    

    def _increaseSizeBy(self, factor = 2):
        new_arr = Array( len(self._items)*factor )
            
        for i in range(self._numItems):
            new_arr[i] = self._items[i]
        
        self._items = new_arr

    def _decreaseSizeBy(self, factor):
        assert self._numItems <= len(self._items)/factor, 'Cannot free still in-use memory.'
        
        new_arr = Array( len(self._items)/factor )

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
                for i in range(self._numItems - 1, position - 1, -1):
                    self._items[i + numElements] = self._items[i]
            else:
                self._increaseSizeBy(2)
                for i in range(self._numItems - 1, position - 1, -1):
                    self._items[i + numElements] = self._items[i]
        else:
            assert self._numItems - position >= abs(numElements), 'Cannot shift left beyond index 0.'
            
            for i in range(position + 1, self._numItems, 1):
                    self._items[i + numElements] = self._items[i]

    def __repr__(self):
        ret = '['
        for i in self:
            ret += f'{i}, '
        if self._numItems > 0:
            ret = ret[:-2]
        ret += ']'
        return ret

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


if __name__ == '__main__':
    v = Vector()
    print(v)

    for i in range(20):
        v.append(i)

    print('append')
    print(v)

    print(f'vector length is {len(v)}')

    print('contains')
    print(v.contains(0))
    print(v.contains(20))
    
    print('get, set')
    print(v[19])
    v[19] = 91
    print(v[19])
    
    print('insert')
    v.insert(5, 100)
    print(v)
    print(f'vector length is {len(v)}')
    v.insert(0, 200)
    print(v)
    print(f'vector length is {len(v)}')
    v.insert(len(v)-1, 300)
    print(v)
    print(f'vector length is {len(v)}')

    print('remove')
    v.remove(6)
    print(v)
    print(f'vector length is {len(v)}')

    print('remove')
    v.remove(0)
    print(v)
    print(f'vector length is {len(v)}')

    print('remove')
    v.remove(len(v)-1)
    print(v)
    print(f'vector length is {len(v)}')

    print('remove')
    v.remove(len(v)-1)
    print(v)
    print(f'vector length is {len(v)}')

    print('indexOf')
    v.indexOf(18)

    print('extend')
    v1 = Vector()
    for i in range(19, 24, 1):
        v1.append(i)

    v.extend(v1)
    print(v)
    print(f'vector length is {len(v)}')

    v1 = v.subVector(10, 20)
    print(v1)
    print(f'vector length is {len(v1)}')