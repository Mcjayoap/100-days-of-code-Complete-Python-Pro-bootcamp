#!/usr/bin/python3
"""
=================
Leap year
=================
This programme works out whether if a given year is a leap year.

This is how you work out whether if a particular year is a leap year.
on every year that is evenly divisible by 4
**except** every year that is evenly divisible by 100
**unless** the year is also evenly divisible by 400
"""

year = int(input("Which year do you want to check? "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Leap year.")
else:
    print("Not leap year.")
