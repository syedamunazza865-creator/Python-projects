import random
import time
print("Welcome to the Dice game!")
time.sleep(3)
rollagain="yes"
while rollagain=="yes":
    print("Rolling the dice...")
    time.sleep(3)
    dice1=random.randint(1,6)
    print("Dice1 is",dice1)
    time.sleep(3)
    dice2=random.randint(1,6)
    print("Dice2 is",dice2)
    time.sleep(3)
    print("Total is",dice1+dice2)
    time.sleep(3)
    rollagain=input("Do u want to roll again?")
