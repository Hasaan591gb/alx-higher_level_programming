#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as exe:
        from sys import stderr
        print("Exception: {}".format(exe), file=stderr)
        return None
