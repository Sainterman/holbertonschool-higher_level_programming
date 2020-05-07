#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    aux_tupA = tuple_a
    aux_tupB = tuple_b
    if len(tuple_a) == 0:
        aux_tupA = (0, 0)
    elif len(tuple_a) == 1:
        aux_tupA = (tuple_a[0], 0)
    if len(tuple_b) == 0:
        aux_tupB = (0, 0)
    elif len(tuple_b) == 1:
        aux_tupB = (tuple_b[0], 0)
    new_tuple = (aux_tupA[0] + aux_tupB[0], aux_tupA[1] + aux_tupB[1])
    return new_tuple
