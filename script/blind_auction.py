# Secret Auction Program
# A Python-based auction system where multiple users
# can submit bids anonymously. The program stores bids,
# compares them, and announces the highest bidder as
# the winner. This project demonstrates dictionaries,
# loops, user input handling, and comparison logic.


bidders ={}
while True :
    name = input("Please enter your name: ").lower()
    bid = int(input("Please enter your bid: "))
    
    bidders [name] = bid
    
    other_player = input(" Are there any other players in the game 'yes' or 'no': ").lower()
    if other_player == "yes":
        print("\n"* 100)
    elif other_player == "no":
        break

  
print(bidders)
highest = 0
winner = ""
for name, cash in bidders.items():
    if highest < cash:
        highest = cash
        winner = name
    else:
        highest

print(f"the highest bid is {highest}")

print(f"the winner is {winner}")


