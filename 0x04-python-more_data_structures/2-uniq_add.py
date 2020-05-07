#!/usr/bin/python3
def uniq_add(my_list=[]):
    residues = []
    if my_list:
        uniq = 0
        for item in my_list:
            if item not in residues:
                uniq += item
                residues.append(item)
        return uniq
