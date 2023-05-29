#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as exe:
        from sys import stderr
        print("Exception: {}".format(exe), file=stderr)
        return False
