#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    function that deletes the item at a specific position in a list
    """
    if idx in range(len(my_list)):
        del my_list[idx]
    return my_list
