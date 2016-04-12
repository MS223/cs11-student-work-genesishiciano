import random
def player_turn():
    player1= raw_input("What's the first players name?")
    player2= raw_input("what's the second players name?")
print player_turn()
cards=range(2,15)*4
random.shuffle(cards)
print cards
