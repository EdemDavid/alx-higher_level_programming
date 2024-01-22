#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as all_in_together_now:
        print("Exception: {}".format(all_in_together_now), file=sys.stderr)
        return None
