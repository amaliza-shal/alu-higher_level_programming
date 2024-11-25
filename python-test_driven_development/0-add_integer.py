#!/usr/bin/python3
<<<<<<< HEAD
# function that adds 2 integers
"""
    Define 'add_integer' function.
"""


def add_integer(a, b=98):
    """
        Return: Sum of integers a & b.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
=======
'''a function that adds 2 integers.'''


def add_integer(a, b=98):
    ''' Function that adds two integers
    Args:
        a : this must be either an integer or float
        b : Must be either an integer or float, and if not provided
            it takes the defualt value of 98
    Returns:
        an integer: the addition of a and b
    '''
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")

    return a + b
>>>>>>> b6ef3d090fa007743bb476cbdcfd6a53531b81fb
