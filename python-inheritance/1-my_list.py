#!/usr/bin/python3
'''This file creates a class that inherits from the built-in list function'''

class MyList(list):
    '''This class inherits the built-in list class and adds the print_sorted method'''

    def print_sorted(self):
        '''Prints the list in sorted order'''
        print(sorted(self))

