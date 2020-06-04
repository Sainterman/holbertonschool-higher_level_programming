#!/usr/bin/python3
""" Script that adds all the arguments to a python list
    then save them to a file
"""
import sys
import os.path

saveToJSON = __import__('7-save_to_json_file').save_to_json_file
loadFromJSON = __import__('8-load_from_json_file').load_from_json_file

if __name__ == "__main__":

    filename = 'add_item.json'
    if os.path.exists(filename):
        newData = loadFromJSON(filename) + sys.argv[1:]
        saveToJSON(newData, filename)
    else:
        newData = sys.argv[1:]
        saveToJSON(newData, filename)
