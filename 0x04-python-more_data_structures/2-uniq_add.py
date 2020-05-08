#!/usr/bin/python3
def uniq_add(my_list=[]):
    residues = []
    uniq = 0
    if my_list:
        for item in my_list:
            if item not in residues:
                uniq += item
                residues.append(item)    
    return uniq
