#Hogwarts
#Program asks for a name amd assigns that person to one of the four harry potter house
#Init
import time
import random
house = ["GRYFFINDOR!", "HUFFLEPUFF!", "RAVENCLAW!", "SLYTHERIN!"]
random_element= random.choice(house)
#Functions
def house(name):
    if name == "harry" or name == "hermione" or name == "ron":
        return("GRYFFINDOR!")
    elif name == "newt" or name == "nymphadora" or name == "pomona":
        return("HUFFLEPUFF!")
    elif name == "Luna" or name == "Cho" or name == "Filius":
        return("RAVENCLAW!")
    elif name == "Voldemort" or name =="draco" or name == "severus":
        return("SLYTHERIN!")
    else:
        return(random_element)


def main():
    print("Welcome to Hogwarts")
    name = input ("Provide your name: ")
    print("..")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("....")
    time.sleep(1)
    print(house(name))
    return

main()
