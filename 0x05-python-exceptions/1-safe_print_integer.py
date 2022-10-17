#!/usr/bin/python3
def safe_print_integer(value):
    successful = False
    try:
        print("{:d}".format(value))
        successful = True
    except Exception:
        successful = False

    return successful
