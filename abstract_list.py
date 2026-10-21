# abstract_list.py
from abc import ABC, abstractmethod


class AbstractList(ABC):
    """The contract every list in this course satisfies."""

    @abstractmethod
    def add(self, element): ...

    @abstractmethod
    def remove(self, index): ...

    @abstractmethod
    def get(self, index): ...

    @abstractmethod
    def set(self, index, element): ...

    @abstractmethod
    def getIndex(self, element): ...

    @abstractmethod
    def size(self): ...
