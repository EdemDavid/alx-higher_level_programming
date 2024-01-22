#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    all_in_together_now = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            all_in_together_now += 1
        except (ValueError, TypeError):
            pass
    print()
    return all_in_together_now
