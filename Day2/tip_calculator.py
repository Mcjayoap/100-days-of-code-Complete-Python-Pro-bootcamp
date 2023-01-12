#!/usr/bin/python3
"""
=======================================
TIP CALCULATOR
=======================================
This programme calculates the value a tip payable by a group of friends from bill


Welcome to the tip calculator!
What was the total bill? $150
What percentage tip are you likely to give? 10, 12, or 15? 12
How many people to split the bill? 5
Each person should pay: $33.6
"""

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? $")
tip = input("What percentage tip are you likely to give? 10, 12, or 15? ")
percent_tip = int(total_bill) * (int(tip) / 100)
share = input("How many people to split the bill? ")
payment = (int(total_bill)  + (percent_tip)) / int(share)
share_amount = "{:.2f}".format(payment)
print(f"Each person should pay: ${share_amount}")
