#!/usr/bin/python3
def no_c(my_string):
    length = len(my_string)

    j = 0

    expd_string = my_string[:]

    for i in range(length):
        if (expd_string[i] == 'c' or my_string[i] == 'C'):
            expd_string = expd_string[:(i - j)] + my_string[(i + 1):]
            j += 1

    return (expd_string)
