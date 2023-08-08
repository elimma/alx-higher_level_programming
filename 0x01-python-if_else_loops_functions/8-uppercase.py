#!/usr/bin/python3
def uppercase(str):
    upp_str = ""
    for c in str:
        if  c.islower():
            upp_str += c.upper()
        else:
            upp_str += c
    return upp_str
