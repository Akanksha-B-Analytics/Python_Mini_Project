# Simple Calculator Program
# A Python calculator that performs basic arithmetic
# operations such as addition, subtraction,
# multiplication, and division. Users can continue
# calculations with previous results or start a new
# calculation. This project demonstrates functions,
# dictionaries, loops, and recursion.


import art

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2
operation_symbols = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}
def caclulator(): ##function calculator
    print(art.logo)
    num1= int(input("Enter the first number: "))

    while True:

        for key in operation_symbols.keys():
          print(f"{key}")
        choice_operation=input("choose any operation you wanna perform")
        num2 = int(input("Enter the another number: "))
        print(F"{num1}  {choice_operation} {num2} is = ")
        ans= operation_symbols[choice_operation](num1, num2)
        print(operation_symbols[choice_operation](num1, num2))
        choice_continue=input("do you want to continue? (y/n) ")
        if choice_continue =="y":
            num1= int(ans)
        else :
            print("\n" * 20)
            caclulator() ##Recursion

caclulator() #calling the funtion
