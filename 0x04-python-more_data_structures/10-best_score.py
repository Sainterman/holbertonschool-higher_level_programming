#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    value = max(sorted(a_dictionary.values()))
    for key, score in a_dictionary.items():
        if score is value:
            return key
