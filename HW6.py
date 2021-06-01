"""Homework 6 for CSE-41273"""
# Adam Vickter
# You need to import something from itertools:
from itertools import cycle


# 1. separate
# Create your own arguments to match the instructions.
def separate(string, sort=False):
    """Return a list of all characters in given string.
        If keyword argument sort is True, then return them sorted."""
    results = []
    for item in string:
        item = item.lower()
        results.append(item)
    if sort:
        results.sort()
    return results


# 2. number_of_vowels
def number_of_vowels(string):
    """Returns the number of vowels in the input string."""
    count = 0
    for item in string:
        item = item.lower()
        if item == 'a' or item == 'i' or item == 'e' or item == 'o' or item == 'u':
            count = count + 1
    return count


# 3. special_nums
def special_nums():
    """Return a generator that yields, in order, the numbers that:
        Are in the range from 1 to 300 and are evenly divisible by 10 and 6."""
    for item in range(1, 301):
        if item % 10 == 0 and item % 6 == 0:
            yield item


# 4. evens
def evens(sequence):
    """Return a generator that returns all the input numbers that are even."""
    for item in sequence:
        if item % 2 == 0:
            yield item


# 5. continuous1234
def continuous1234():
    """Return a generator that returns the numbers 1, 2, 3, 4 continuously."""
    lst = [1, 2, 3, 4]
    result_list = cycle(lst)
    for number in result_list:
        yield number


# 6. reverse_iter
def reverse_iter(iterable):
    """Return a generator that yields items from iterable in reverse order"""
    length = len(iterable) - 1
    while length >= 0:
        yield iterable[length]
        length = length - 1


# 7. ReverseIter class
class ReverseIter:
    """Class whose instances iterate the initial iterable in reverse order"""

    def __init__(self, sequence):
        self.sequence = sequence
        self.index = len(sequence)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > 0:
            self.index = self.index - 1
            return self.sequence[self.index]
        else:
            raise StopIteration

    def next(self):
        return self.__next__()
