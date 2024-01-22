#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
    except Exception as all_in_together_now:
        sys.stderr.write("Exception: {}\n".format(all_in_together_now))
        return (False)
    else:
        return (True)
