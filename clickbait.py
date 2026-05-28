#susie
#Clickbait
#Takes in information and generates clickbait headlines

#Init
#Functions
#Main
name = input ("Please enter your name: ")
print ("Hello " + name + "!")
def headline1():
    topic = input ("What would you like tips on? (e.g. baking, gaming, writing, etc...): ")
    number = input ("How many tips would you like to recieve? ")
    print (f"Here's {number} tips on how to be the best at {topic}! Don't believe me? Read here.")
def headline2():
    musician = input ("Who is your favorite musician/band?")
    number = input ("I can expose as many things about them as you would like. How many facts would you like to read about them?")
    print (f"Did you know that {musician} is cancelled? Here's {number} reasons why!!")
def headline3():
    topic = input ("What is something you hate doing? ")
    topic2 = input ("What is something you love doing? ")
    print (f"Here's 8 reasons why you need to stop  {topic2} and start  {topic}!")
headline1()
headline2()
headline3()
