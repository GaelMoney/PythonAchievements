import sys
import time

def callMe(name, number):
    print("&: Hello?")
    time.sleep(1)
    print("&: Who are you?")
    time.sleep(1)
    print("*: It's me "+ name)
    time.sleep(1)
    print("&: Hi "+ name+ " I'm sorry I'm busy right now can I call you back?")
    time.sleep(1)
    print("*: alright here is my number "+ number)
    time.sleep(1)
    print("&: speak to you in a bit "+ name)
    time.sleep(1)
    print("&: hey wait "+ name+ " from highschool?")
    time.sleep(1)
    print("*: thats right its me!")
    time.sleep(1)
    print("&: OH my god it really has been a long time hasnt it?!")
    time.sleep(1)
    print("*: yes it really has been I wa-....hold on im getting a call you got my number right?")
    time.sleep(1)
    print("&: yeah I got it "+ number+ " speak to you later then")
    time.sleep(1)
    print("*: cya")

    
print(sys.argv)
callMe(sys.argv[1], sys.argv[2])
