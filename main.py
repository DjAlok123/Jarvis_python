import random
import os

sanjai = True

print("type all the commands in small letters")
print("Ask me whatever you want")

while sanjai:
    jarvis = input("> ")

    if jarvis == "help me":
        print('''hi
what is your name
what is the full form of jarvis
cls
tell me my future
off
tell me a joke
who is your programmer
    ''')

    if jarvis == "tell me a joke":
        random_joke = ['Q. What do you call a train carrying bubblegum? A. A chew chew train']
        print(random.choice(random_joke))


    if jarvis == "who is your programmer":
        print("It's DjAlok123")

    if jarvis == "hi":
        print("hi!")
            
    if jarvis == "what is your name":
            print("I Am J.A.R.V.I.S, I am your personal assitant")
            pass

    if jarvis == "what is the full form of jarvis":
        print("Just A Rather Very Intelligent System")

    if jarvis == "cls":
        os.system('clear')

    if jarvis == "tell me my future":
        random_future = ["I hope it would be a great day", "You have a bright future", "Wonderful life is ahead of you"]
        print(random.choice(random_future))

    if jarvis == "off":
        print("As you wish, sir!")
        break      
    
