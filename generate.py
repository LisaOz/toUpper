from random import choice
import random

coin = choice(["heads", "tails"])
print(coin)

print("***********************")
number = random.randint(1, 10)
print(number)

print("***********************")
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
    