#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    all_in_together_now = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            all_in_together_now += 1
        except IndexError:
            break
    print()
    return all_in_together_now
