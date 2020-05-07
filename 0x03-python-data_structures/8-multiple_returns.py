#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        info = (0, None)
    else:
        info = (len(sentence), sentence[0])
    return info
