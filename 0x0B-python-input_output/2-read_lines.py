#!/usr/bin/python3
""" read n amopunt of lines from text file """


def read_lines(filename="", nb_lines=0):
    """ open, check amount of lines, read and print """
    with open(filename, encoding='utf-8') as f:
        if nb_lines <= 0:
            text = f.read()
            print(text)
        else:
            for i in range(nb_lines):
                print(f.readline(), end="")
