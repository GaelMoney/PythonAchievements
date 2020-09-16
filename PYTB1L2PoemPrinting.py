vers1 = "Gael Griffith is wie ik ben."


vers2 = "Osdorp is waar ik woon."


vers3 = "Game development is mijn droom."


vers4 = "Ik heb een hekel aan een drone."


vers5 = "Mijn droom is hoog, maar mijn gezondheid hoger."

print(vers1,vers2,vers3,vers4,vers5)

while True: 
    query = input('wil je dit opnieuw lezen? Y/N')
    Fl = query[0].lower()
    if query == '' or not Fl in ['y','n']:
      	print('Antwoord met yes of nee thanks!')
    else: break
if Fl == 'y':
    print("here we go!")
if Fl == 'n':
    print("aawhh jammer bye bye")
