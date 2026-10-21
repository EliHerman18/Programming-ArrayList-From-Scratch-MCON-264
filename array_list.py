# array_list.py
from abstract_list import AbstractList


class ArrayList(AbstractList):



    #Max possible length of list
    CAPACITY = 100

    #A list built on a fixed block of 100 cells.
    def __init__(self):
        self._array = [None] * 100
        self._size = 0

    def add(self, element):
        #Store element in the first free cell. Raises OverflowError when full.
        if self._size >= self.CAPACITY:
            raise OverflowError("ArrayList is full (capacity 100)")
        self._array[self._size] = element
        self._size += 1

    def remove(self, index):
        #Remove and return the element at index, shifting later elements left.
        self._check_index(index)
        removed = self._array[index]
        # Moving each element forward one.
        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]
        # Blank the cell left behind at the end.
        self._array[self._size - 1] = None
        self._size -= 1
        return removed

    def get(self, index):
        #Returns index (if valid index)
        self._check_index(index)
        return self._array[index]

    def set(self, index, element):
        #sets index to element (if valid index)
        self._check_index(index)
        self._array[index] = element

    def getIndex(self, element):
        for i in range(self._size):
            if self._array[i] == element:
                return i
        return -1

    def size(self):
        """Return the number of stored elements (a maintained counter)."""
        return self._size

    def _check_index(self, index):
        if index < 0 or index >= self._size:
            raise IndexError(f"index {index} is out of range for size {self._size}")