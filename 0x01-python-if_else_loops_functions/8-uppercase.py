#!/usr/bin/python3
def uppercase(str):
    uppercased_str = ""
  for c in str:
    if c.islower():
      uppercased_str += c.upper()
    else:
      uppercased_str += c

  return uppercased_str
