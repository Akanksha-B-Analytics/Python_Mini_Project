# --------------------------------------------------
# Coffee Machine Simulation
#
# A command-line coffee machine program built with
# Python that allows users to order different coffee
# drinks, process payments, and manage available
# resources. The machine checks ingredient availability,
# handles coin transactions, and updates inventory
# after each successful purchase.
#
# Features:
# - Multiple drink options (Espresso, Latte, Cappuccino)
# - Resource availability checking
# - Coin-based payment processing
# - Change calculation and refunds
# - Profit tracking
# - Resource usage and inventory updates
# - Machine status report
#
# Concepts Used:
# - Dictionaries and Nested Dictionaries
# - Functions
# - Loops (while)
# - Conditional Statements
# - Global Variables
# - User Input and Output
# - Resource Management Logic
#
# This project was created to practice Python
# fundamentals while simulating a real-world coffee
# vending machine system with inventory and payment
# handling.
# --------------------------------------------------


from importlib.resources import is_resource
from tkinter import Menu

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def is_resource_sufficient(order_ingredients) :
 """Return True when order can be made , False when the order is insufficient """
 for item in order_ingredients:
     if order_ingredients[item] >= resources[item]:
         print(f"Sorry there is not enough {item}.")
         return False
     return True

def process_coin():
 """Returns the total calculated form coins inserted"""
 print("Please insert the coins")
 total= int(input("How many quarters"))*0.25
 total+=int(input("How many dimes?"))* 0.10
 total+=int(input("How many nickels?"))* 0.5
 total+=int(input("How many pennies?"))* 0.1
 return total

def is_transaction_successfull(money_received, drink_cost) :
  """Return True when transaction is accepted or False if the transaction is failed"""
  if money_received >= drink_cost:
      global profit
      profit += drink_cost
      change = round(money_received - drink_cost,2)
      print(f"Here is the change ${change}.")
      return True
  else:
      print(f"Sorry there is not enough money. Your ${money_received} is refunded")
      return False
def make_coffee(drink_name, order_ingredients) :
 for item in order_ingredients:
   resources[item] -= order_ingredients[item]
   print(f"Here is your {drink_name} ")
   return


is_on = True
while is_on:
  choice=(input( "What would you like? (espresso/latte/cappuccino): "))
  if choice == "off":
    is_on = False
  elif choice=="report":
      print(f"Water: {resources['water']}ml")
      print(f"Milk:{resources['milk']}ml")
      print(f"Coffee:{resources['coffee']}g")
      print(f"Money: ${profit}")
  else :
      drink= MENU[choice] ##MENU[latte]--output ingredients{water,milk..} cost:2.5..
      print(drink)
      if is_resource_sufficient(drink["ingredients"]):##only for checking
        payment= process_coin() ##returns total money given
        if is_transaction_successfull(payment, drink["cost"]):##process the total and returns change
           make_coffee(choice, drink["ingredients"])
