vers1 = "Gael Griffith is wie ik ben."


vers2 = "Osdorp is waar ik woon."


vers3 = "Game development is mijn droom."


vers4 = "Ik heb een hekel aan een drone."


vers5 = "Mijn droom is hoog, maar mijn gezondheid hoger."

print(vers1,vers2,vers3,vers4,vers5)

Fl = ""

while True:
	query = input('wil je dit opnieuw lezen? Y/N')
	if len(query) > 0:
		Fl = query[0].lower()
		if Fl != 'y' and Fl != 'n':
			print('Antwoord met yes of nee thanks!')
		else: break
	else: break

if Fl == 'y':
	print("here we go!")
elif Fl == 'n':
	print("aawhh jammer bye bye")
