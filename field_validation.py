"""
Helper module to handle string validation stuff that I noticed I had to do
everywhere. It is a given for all functions that they will only be handed strings
(thus no type checking is necessary).
"""

import string


def is_letter(string_):
    """
    Checks if provided string is a single letter.
    Examples:
    "a" --> True
    "C" --> True
    "2" --> False
    """
    if string_ not in string.ascii_letters or len(string_) > 1:
        return False
    return True


def is_date(string_):
    """
    Checks if provided string is a valid date. Valid in this case also means that
    month and day can be either zero padded or not, but year may not be
    abbreviated. However, will NOT check for value ranges in date.
    Examples:
    "10/21/2017" --> True
    "4/1/1988" --> True
    "05/08/2015" --> True
    "5/68/2000" --> True
    "04201966" --> False
    """
    date = string_.split("/")
    if len(date) != 3:
        return False
    if len(date[2]) != 4:
        return False
    return True


def is_bool(string_):
    """ Checks if provided string has some kind of a boolean meaning. """
    bools = ["yes", "y", "1", "no", "n", "0"]
    if string_.lower() in bools:
        return True
    return False


def is_rate(string_):
    try:
        float(string_)
    except ValueError:
        return False
    else:
        return True
