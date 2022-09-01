#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_symbol = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if (roman_string is None) or (type(roman_string) is not str):
        return 0

    num = len(roman_string)
    to_int = roman_symbol[roman_string[num-1]]
    for i in range(num - 1, 0, -1):
        insrt_roman_value = roman_symbol[roman_string[i]]
        real_roman_value = roman_symbol[roman_string[i-1]]

        if real_roman_value >= insrt_roman_value:
            to_int += real_roman_value
        else:
            to_int -= real_roman_value
    return to_int
