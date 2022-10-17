#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    successful = False
    try:
        print("{:d}".format(value))
        successful = True
    except Exception as exep:
        print("Exception: {}".format(exep), file=sys.stderr)
    return successful
