#Creates a slot machine
#Init
import random
symbols = ["7","✷","☽","♡"]
weights = [5, 15, 35, 45]
credits = 0
def machine():
    output = []
    global credits
    for i in range (3):
        output.append(random.choices(symbols, weights=weights, k=1)[0])
    print(output)
    if output == ["7","7","7"]:
        print("JACKPOT!!! You win!")
        credits = credits + 500
    elif output == ["✷","✷","✷"] or output == ["☽","☽","☽"] or output == ["♡","♡","♡"]:
        print("Winner, winner, chicken dinner!")
        credits = credits + 100
    else:
        print("LOSER")
        credits = credits - 10
def deposit():
    global credits
    dep = input("Select your deposit: 50, 100, 500 ")
    if dep == "50":
        credits = credits + 50
    elif dep == "100":
        credits = credits + 100
    elif dep == "500":
        credits = credits + 500
    else:
        print("not a valid deposit value.")


while True:
    print (f"You have {credits} credits")
    if credits >= 10:
        begin = input("Type s to TEST YOUR LUCK at the peysie slot machine! ")
        if begin == "s" or begin == "S":
            machine()
        else:
            break
    else:
        print("INSUFFICIENT FUNDS. PLEASE INSERT CREDITS")
        deposit()
def odds():
    wins = 0
    losses = 0
    for i in range (1000):
        output = []
        pmoney = 0
        cmoney = 0
        for i in range (3):
            output.append(random.choices(symbols, weights=weights, k=1)[0])
        if output == ["7","7","7"]:
            pmoney = pmoney + 490
            cmoney = cmoney -490
        elif output == ["✷","✷","✷"] or output == ["☽","☽","☽"] or output == ["♡","♡","♡"]:
            pmoney = pmoney + 90
            cmoney = cmoney - 90
        else:
            pmoney = pmoney - 10
            cmoney = cmoney + 10
    print (f"Total player profit: {pmoney}. Total casino profit: {cmoney}")

