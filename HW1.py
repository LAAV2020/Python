"""Homework 1 for CSE-41273"""
"Adam Vickter"

from textwrap import dedent


# Function 1
def silly_case(in_string):
    """Given a string, convert it to a string such that each word starts with
        a lower case letter, and the remaining letters are uppercase.
        Return the silly case string."""
    wordList= [word.capitalize().swapcase() for word in in_string.split(" ")]

    return " ".join(wordList)


# Function 2
def dash_stringify(word_list):
    """Given a list of word strings, return a single string with all the
        strings together, with ' - ' in between the words."""
    return ' - '.join(word_list)


# Function 3
def is_perfect_square(number):
    """Given a number, return True if it is a perfect square,
        else return False"""
    return int(number ** 0.5)**2 == number


# Function 4
def comfort_level(temperature):
    """Given a temperature in Fahrenheit, comment on the comfort level"""
    if temperature > 82:
        return "Too hot"
    if temperature > 74:
        return "A bit warm"
    if temperature < 60:
        return "Too cold"
    if temperature < 70 and temperature >= 60:
        return "A bit chilly"
    return "A comfortable temperature"


# Function 5
def dict_from_triple(tuples):
    """Given a list of 3-tuples, return a dictionary whose keys are the first
        elements of the tuples, and the values are tuples containing the
        corresponding second and third elements of the tuples."""

    result = dict()
    for triple in tuples:
        result[triple[0]] = (triple[1], triple[2])
    return result


# Function 6
def get_oldest(date1, date2):
    """Given 2 date strings in "MM/DD/YYYY" format, return oldest one."""
    "YYYY/MM/DD"
    datearr1 = date1.split('/')
    datearr2 = date2.split('/')
    d1 = "".join([datearr1[2]] + datearr1[:-1])
    d2 = "".join([datearr2[2]] + datearr2[:-1])
    if d1 > d2:
        return date2
    return date1
