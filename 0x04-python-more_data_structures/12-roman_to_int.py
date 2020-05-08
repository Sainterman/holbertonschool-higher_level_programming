#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    romans = dict([("I", 1), ("V", 5), ("X", 10), ("L", 50), ("C", 100),
                  ("D", 500), ("M", 1000)])
    number = 0
    ultimo = 0
    for i in roman_string:
        for roman in romans:
            if i is roman:
                actual = romans[roman]
                if ultimo is 0 or ultimo >= actual:
                    number += actual
                elif ultimo < actual:
                    number += actual - (ultimo * 2)
                ultimo = actual
    return number
