"""Homework 2 for CSE-41273"""
# Adam Vickter


# Function 1
def combine_lists(one, two):
    """Take 2 lists as input and return a new list consisting of the elements
        of the first list followed by the elements of the second list."""
        
    combine_lists = one + two
    return(combine_lists)

    
# Function 2
def last_n_elements(sequence, n):
    """Given a sequence and a number n, return the last n elements of the
        sequence."""
    Apple = sequence[-n:]
    return Apple


# Function 3
def last_n_reversed(sequence, n):
    """Given a sequence and a number n, return the last n elements of the
        sequence in reversed order."""

    return sequence[-n:][::-1]




# Function 4
nList = [1,4,7,2,9]
def power_list(numbers):
    """Given a list of numbers, return a new list where each element is the
        corresponding element of the list to the power of its list index."""
    numbers2 = []
    for idx, val in enumerate(numbers):
        number2 = val**idx
        numbers2.append(number2)
    return(numbers2)
  
    
# Function 5
def rotate_list(some_list):
 """Take a list as input and remove the first item from the list and add it
 to the end of the list. Return the item moved"""
 first = some_list.pop(0)
 some_list.append(first)
 return first


 # Function 6
def get_vowel_names(names):
    """Return a list containing all names given that start with a vowel."""
    new_list = []
    for name in names:
        if name[0].lower() in 'aeiou':
            new_list.append(name)
    return(new_list)

