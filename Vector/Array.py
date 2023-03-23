from ctypes import py_object

class Array():
    def __init__(self, size):
        assert size > 0, 'Size must be greater than 0.'
        self._size = size
        pyArrayType = py_object * size # creates pyArray structure
        self._elements = pyArrayType() # init the structure
        self.clear(None)

    def __len__(self):
        return self._size
    
    def __getitem__(self, index):
        assert index >= 0 and index < self._size, "Array subscript out of range."
        return self._elements[index]
    
    def __setitem__(self, index, value):
        assert index >= 0 and index < self._size, "Array subscript out of range."
        self._elements[index] = value

    def clear(self, value):
        for i in range(self._size):
            self._elements[i] = value

    def __iter__(self):
        return _ArrayIterator(self._elements)
    
    def __repr__(self):
        ret = '['
        for e in self:
            ret += f'{e}, '
        ret = ret[:-2]
        ret += ']'
        return ret
    

class _ArrayIterator():
    def __init__(self, array):
        self._array = array
        self._curNdx = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._curNdx < len(self._array):
            element = self._array[self._curNdx]
            self._curNdx += 1
            return element
        else:
            raise StopIteration
        
if __name__ == '__main__':
    arr = Array(10)
    
    for i in range(10):
        arr[i] = 10 - i
    
    print(arr)

    print(len(arr))

    arr[0] = 100

    print(arr)