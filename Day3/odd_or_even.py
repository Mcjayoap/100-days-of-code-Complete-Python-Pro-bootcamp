#!/usr/bin/python3
"""
========================
Odd or Even
========================
Programme works out whether if an inputed number is even or odd.
"""

number = int(input("Which number do you want to check? "))

if (number % 2) == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
