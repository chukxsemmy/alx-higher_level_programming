#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    newStr = ""
    for ch in str:
        if i != n:
            newStr += ch
        i += 1
    return newStr
