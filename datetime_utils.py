"""
Helper module to handle various datetime object building that I was doing all
over the place.
"""

import datetime


def build_date():
    """ Builds datetime.date object. """
    while True:
        date = input("Enter date in MM/DD/YYYY format (leave blank for today)\n")
        if not date:
            date_obj = datetime.date.today()
            return date_obj
        else:
            try:
                date = date.split('/')
                date_obj = datetime.date(int(date[2]), int(date[0]), int(date[1]))
                return date_obj
            except IndexError:
                print("Invalid entry (check format?)")
            except ValueError as e:
                print("Invalid entry ({})".format(e))


def build_time(of=None):
    """ Builds datetime.time object, with of specifying what the builder should
    say it is building the time of (e.g. of="start" --> "Start hour?") """
    h = m = p = None
    while h is None or m is None or p is None:
        if h is None:
            try:
                h = int(input("{0} hour?\n".format(of.capitalize())))
                assert 1 <= h <= 12
            except ValueError:
                print("Invalid entry: input a valid number.")
                h = None
                continue
            except AssertionError:
                print("Invalid entry: hour must be in range 1-12.")
                h = None
                continue
        if m is None:
            try:
                m = input("{0} minute? (default :00)\n".format(of.capitalize()))
                if m == "":
                    m = 0
                m = int(m)
                assert 0 <= m <= 59
            except ValueError:
                print("Invalid entry: input a valid number.")
                m = None
                continue
            except AssertionError:
                print("Invalid entry: minute must be range 0-59 or blank.")
                m = None
                continue
        if p is None and h is not None:
            try:
                p = input("AM or PM? (default PM)\n")
                assert p.upper() in ["AM", "A", "PM", "P", ""]
                if p.upper() in ["PM", "P", ""] and h != 12:
                    h += 12
                if p.upper() in ["AM", "A"] and h == 12:
                    h -= 12
            except AssertionError:
                print("Invalid entry: must be either AM, PM or blank.")
                p = None
                continue
    return datetime.time(h, m)


def get_start_of_month():
    now = datetime.datetime.now()
    return datetime.date(now.year, now.month, 1)


def get_end_of_month():
    now = datetime.datetime.now()
    return datetime.date(now.year, now.month + 1, 1) - datetime.timedelta(days=1)


def get_start_of_week():
    now = datetime.datetime.now()
    return datetime.date(now.year, now.month, now.day - now.weekday())


def get_end_of_week():
    now = datetime.datetime.now()
    return get_start_of_week() + datetime.timedelta(days=6)
