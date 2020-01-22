#!/usr/bin/python3
""" import JSON representation """
import json


def load_from_json_file(filename):
    """ creates an Object from a “JSON file” """
    with open(filename, "r") as f:
        json.load(f)
