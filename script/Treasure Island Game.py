# --------------------------------------------------
# Treasure Island Adventure Game
#
# A simple text-based adventure game built in Python.
# Players make a series of choices to navigate through
# different challenges in search of hidden treasure.
#
# This project demonstrates the use of:
# - User input
# - Conditional statements (if/elif/else)
# - Nested decision-making
# - Basic game logic
#
# Created as a beginner-friendly Python project.
# --------------------------------------------------



print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1=input('Choose any direction :- "Left" or "Right"').lower()
if choice1 == "left":
    print('Congratulations you\'ve  made it to the next level')
    choice2= input(' There is a lake in front of'
                   ' you ,choose if you wanna "wait" for the boat or "swim"')
    if choice2 == "wait":
        print('Congratulations you\'ve made it to the shore safely')
        choice3= input('Now this is the last stage of the game ,'
                       'be carefull while choosing the door,'
                       '"Blue","Yellow","Red"')
        if choice3 == "blue":
            print('Congratulations you\'re the WINNER , you\'ve found the treasure')
        elif choice3 == "yellow":
            print('OH no , you got poisoned by toxic gas,GAME OVER')
        else :
            print('OH no, the RED HOT FIRE got you, GAME OVER')

    else:
        print( 'OH!NOOO , you\'ve got eaten by alligators, GAME OVER')
else :
    print('You fell in a well ,GAME OVER')
