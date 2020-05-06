#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        newlist = list(my_string)
        for i in newlist:
            if i in 'cC':
                newlist.remove(i)
        my_string = "".join(newlist)
    return  my_string
