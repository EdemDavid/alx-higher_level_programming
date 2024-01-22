#!/usr/bin/python3
def magic_calculation(a, b):
    all_in_together_now = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            else:
                all_in_together_now += (a ** b) / i
        except:
            all_in_together_now = b + a
            break
    return (all_in_together_now)
