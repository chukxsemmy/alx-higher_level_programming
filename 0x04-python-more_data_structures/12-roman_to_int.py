#!/usr/bin/python3
def to_subtract(list_num):
    to_int = 0
    curr = max(list_num)

    for n in list_num:
        if curr > n:
            to_int += n

    return (curr - to_int)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roman_symbol = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(roman_symbol.keys())

    num = 0
    prev = 0
    list_num = [0]

    for ch in roman_string:
        for r_num in list_keys:
            if r_num == ch:
                if roman_symbol.get(ch) <= prev:
                    num += to_subtract(list_num)
                    list_num = [roman_symbol.get(ch)]
                else:
                    list_num.append(roman_symbol.get(ch))

                prev = romand_symbol.get(ch)

    num += to_subtract(list_num)

    return (num)
