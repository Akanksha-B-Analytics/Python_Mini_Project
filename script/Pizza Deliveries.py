 """
Python Pizza Delivery Calculator

Description:
This project is a simple pizza ordering system built using Python.
The program allows users to choose whether they want a pizza,
select a pizza size (Small, Medium, or Large), add pepperoni,
and choose extra cheese. Based on the selected options, the
program calculates and displays the final bill.

Concepts Used:
- User Input
- Variables
- Conditional Statements (if, elif, else)
- Arithmetic Operations
- Program Flow Control

Example Output:

Welcome to Python Pizza Deliveries!
Do you want pizza? Y or N: Y
What size pizza do you want? S, M or L: M
Do you want pepperoni on your pizza? Y or N: Y
Do you want extra cheese? Y or N: Y

Your total bill is: 19


Created as part of my Python learning journey.
"""                    

print("Welcome to Python Pizza Deliveries!")
want_pizza = input("Do you want pizza? Y or N")

bill = 0
if want_pizza == "Y":
    size = input("What size pizza do you want? S, M or L: ")
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    extra_cheese = input("Do you want extra cheese? Y or N: ")
    if size == "S":
        bill = 5

        if pepperoni == "Y":
                bill += 2
    elif size == "M":
        bill = 15

        if pepperoni == "Y":
            bill += 3
    else:
        bill = 20

        if pepperoni == "Y":
            bill += 3


    if extra_cheese == "Y":
       bill += 1
       print( f" Your total bill is : {bill} ")
    else:
       print(f" Your total bill is : {bill} ")
else :
   print("Bye Bye , Thanks for wasting my time!")
