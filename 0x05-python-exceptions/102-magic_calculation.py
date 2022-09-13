#!/usr/bin/python3
def magic_calculation(a, b):
    magic_cal = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too Far')
            else:
                magic_cal += a ** b / i
        except:
            magic_cal  = b + a
            break
    return (magic_cal)
