#creates a gossip girl character based on questions
def nickname():
    a = input("Would you like to be a girl or boy? ")
    if a == "girl":
        b = input("Would you like to be a student or adult? ")
        if b =="student":
            c = input("Would you rather go to a party or study? ")
            if c =="go to a party" or "party":
                print("You are Serena VanDerWoodsen!")
            else:
                print("You are Vanessa Abrams!")
        else:
            d = input("Would you rather be a fashion designer or a socialite? ")
            if d =="fashion designer":
                print("You are Eleanor Waldorf!")
            else:
                print("You are Lily Bass!")
    else:
        e = input("Would you like to be a student or adult? ")
        if e =="student":
            f = input("Would you rather go to a party or study? ")
            if f =="go to a party" or "party":
                print("You are Chuck Bass!")
            else:
                print("You are Dan Humphrey!")
        else:
            g = input("Would you rather be a CEO or a Musician? ")
            if g =="CEO" or "ceo":
                print("You are Bart Bass!")
            else:
                print("You are Rufus Humphrey!")
nickname()

