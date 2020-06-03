#!/usr/bin/python3
""" create class subclass MyList from list """


class MyList(list):
    """
    print_sorted(): print a sorted copy of the list
    using parent class methods
    """

    def __init__(self):
        """ initialize using parent class """
        super().__init__()

    def print_sorted(self):
        """ print using sorted """
        print(sorted(self))
