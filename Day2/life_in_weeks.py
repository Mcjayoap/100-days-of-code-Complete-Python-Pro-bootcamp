#!/usr/bin/python3
"""
==============================
LIFE IN WEEKS CALCULATOR
==============================

This programme calculates how many days,weeks and months we have left if we live until 90 years old.

It will take the user's current age as tge input, and then output a message with his time left to live from 90.
"""


age = input("What is your current age? ")

years_remaining = 90 - int(age)
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")
