#!/usr/bin/python3
"""
The presentation phrase module
==============================
this module has an say_my_name fucn just for now
"""


def say_my_name(first_name, last_name=""):
    """
    Funtion that prints a presentation phrase (his name)
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
