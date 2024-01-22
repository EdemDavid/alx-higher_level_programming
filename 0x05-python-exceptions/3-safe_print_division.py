#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        all_in_together_now = a/b
    except (TypeError, ZeroDivisionError):
        all_in_together_now = None
    finally:
        print("Inside all_in_together_now: {}".format(all_in_together_now))
    return all_in_together_now
