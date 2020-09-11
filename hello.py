import time

a = True
while a == True:
    hello = "Hello, mijn naam is {owner}. Wat is jouw naam?"
    print(hello.format(owner = "Gael Griffith"))

    time.sleep (1)

    username = input("Mijn naam is:")
    print("Goededag " + username, "Hier is de datum")

    time.sleep (1)

    import datetime

    x = datetime.datetime.now()

    print("Vandaag is het " + x.strftime("%d"), "van " + x.strftime ("%B"))
    while True: 
             query = input('Wil je doorgaan? Y/N')
             Fl = query[0].lower()
             if query == '' or not Fl in ['y','n']: 
                print('liever dat je geen antwoord geeft!') 
             else: 
                break 
    if Fl == 'y': 
            print("nee waarom!")
    if Fl == 'n': 
            break