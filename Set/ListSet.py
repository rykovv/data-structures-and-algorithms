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

class _ListSetIterator():
    def __init__(self, theSet):
        self._curSet = theSet
        self._curIter = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._curIter < len(self._curSet):
            el = self._curSet[self._curIter]
            self._curIter += 1
            return el
        else:
            raise StopIteration

class ListSet():
    def __init__(self):
        """Creates a new set initialized to an empty set."""
        self._elements = []

    def __len__(self):
        """Returns the number of elements in the set or its cardinality."""
        return len(self._elements)
    
    def __contains__(self, element):
        """Determines if a given value is an element of the set.

        Args:
            element (Any): Given value

        Returns:
            Boolean: True if contains
        """
        return element in self._elements

    def add(self, element):
        """Modifies the set by adding a given value or element to the set.

        Args:
            element (Any): Given value or an element
        """
        if element not in self._elements:
            self._elements.append(element)

    def remove(self, element):
        """Removes a given value from the set if a member.

        Args:
            element (Any): Given value
        """
        if element in self._elements:
            self._elements.remove(element)

    def __eq__(self, setB):
        """Determines if a set is equal to another set.

        Args:
            setB (Set): Set to be compared with

        Returns:
            Boolean: True if the set is equal
        """
        if len(setB) is not len(self._elements):
            return False
        else:
            return self.isSubsetOf(setB)
        
        return True

    def isSubsetOf(self, setB):
        """Determins if a set is a subset of setB.

        Args:
            setB (Set): Another set

        Returns:
            Boolean: True if a subset
        """
        if len(self._elements) <= len(setB):
            for el in self._elements:
                if el not in setB:
                    return False
        else:
            return False
        
        return True

    def union(self, setB):
        """Creates and returns a new set that is a union of this set and setB

        Args:
            setB (Set): another set

        Returns:
            Set: Union if this set and setB
        """
        newSet = ListSet()
        for el in self._elements:
            newSet.add(el)
        for el in setB:
            newSet.add(el)

        return newSet

    def intersect(self, setB):
        """Creates and returns a new set that is an intersection of this set
        and setB.

        Args:
            setB (Set): Another set

        Returns:
            Set: Intersection of this set and setB
        """
        newSet = ListSet()
        for el in self._elements:
            if el in setB:
                newSet.add(el)
        
        return newSet

    def difference(self, setB):
        """Creates and returns a new set that is a difference of this set and setB

        Args:
            setB (Set): Another set

        Returns:
            Set: Difference set
        """
        newSet = ListSet()
        for el in self._elements:
            if el not in setB:
                newSet.add(el)

        return newSet

    def __iter__(self):
        return _ListSetIterator(self._elements)
    
    def __repr__(self):
        ret = 'Set( '
        for el in self:
            ret += f'{el}, '
        ret = ret[:-2] + ' )'
        return ret

if __name__ == '__main__':
    ls = ListSet()
    for i in range(20):
        ls.add(i)

    print('--- add new')
    print(ls)

    for i in range(20):
        ls.add(i)

    print('--- add dup')
    print(ls)

    print('--- len')
    print( len(ls) )

    print('--- contains')
    print(0 in ls)
    print(20 in ls)

    ls.remove(0)
    ls.remove(19)

    print('--- remove')
    print(ls)

    ls1 = ListSet()
    ls2 = ListSet()

    for i in range(20):
        ls1.add(i)
        if i is not 0 and i is not 19:
            ls2.add(i)

    print('--- eq')
    print(ls == ls1)
    print(ls == ls2)

    ls1 = ListSet()
    for i in range(5, 10, 1):
        ls1.add(i)

    print('--- isSubsetOf')
    print(ls.isSubsetOf(ls1))
    print(ls1.isSubsetOf(ls))

    ls1 = ListSet()
    for i in range(10, 30, 1):
        ls1.add(i)

    print('--- intersect')
    print(ls.intersect(ls1))

    print('--- union')
    print(ls.union(ls1))

    print('--- difference')
    print(ls.difference(ls1))
    print(ls1.difference(ls))