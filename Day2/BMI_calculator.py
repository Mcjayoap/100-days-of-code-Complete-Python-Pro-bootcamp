#!/usr/bin/python3

"""
==============================
Day2 project1: BMI Calculator
==============================

This programme calculates the Body mass index (BMI) from a user's weight and height.

BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m).
"""

height = input("enter your height in m: ")
"""Prompts user to input height"""
weight = input("enter your height in kg: ")
"""Prompts user to enter weight"""
bmi = float(weight) / (float(height) ** 2)
print(int(bmi))
