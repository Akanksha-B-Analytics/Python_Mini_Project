# Tip Calculator

#A simple Python program that calculates the total bill including tip and splits the amount evenly among a group of people.

## Features
#- Calculates tip based on a percentage.
#- Adds tip to the original bill.
#- Splits the total amount among multiple people.
#- Displays the amount each person should pay.

## Technologies Used
##- Python 3

## Example

##Bill: $100
##Tip: 20%
##People: 2
##Total Bill: $120.00
##Each Person Pays: $60.00


print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
total_bill = bill * (tip / 100) + bill
print(f"Your total biil is now $ {total_bill}" )
each = total_bill / people
print(f"Each person should pay: ${each}")

#project completed
