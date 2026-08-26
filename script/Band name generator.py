
# --------------------------------------------------
# Project: Band Name Generator
# Author: Akanksha Borkar
# Repository: Python Mini Projects
# Description:
# A simple Python program that generates a band name
# using user-provided inputs.
#
# Skills Practiced:
# - User Input
# - Variables
# - String Concatenation
#
## Band Name Generator

#Generates a fun band name based on user input.

### Example Output

#```text
#Welcome to the Band Name Generator!

#Whats your city name ?
#Mumbai

#Whats your pet's name?
#Rocky

#Your band name could be: Mumbai Rocky
#```

print("hello " + input("whats your name?\n") + "!")
petname = input("whats your pet's name?\n")
cityname = input("whats your city's name?\n")
print("Your band name is:- " + petname + " " + cityname)


