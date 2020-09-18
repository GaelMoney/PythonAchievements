Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2 + 2
4
>>> 3*10
30
>>> 100-10
90
>>> 25/5
5.0
>>> 10/3
3.3333333333333335
>>> 10//3
3
>>> print('Mijn naam is Gael Griffith')
Mijn naam is Gael Griffith
>>> naam = 'Gael Griffith'
>>> print(naam)
Gael Griffith
>>> print(naam.upper())
GAEL GRIFFITH
>>> print(naam[0:2])
Ga
>>> print(naam[::-1])
htiffirG leaG
>>> leeftijd = 17
>>> print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
Hallo Gael Griffith ben je al 17 jaar?
>>> leeftijd = leeftijd + 1
>>> leeftijd
18
>>> leeftijd-=1
>>> leeftijd
17
>>> if leeftijd < 18:									hoelang_tot18jaar = 18 - leeftijd						print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')		elif leeftijd > 18:									hoelang_al18jaar = leeftijd - 18 						print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')		else:													    print('Het is alweer ' + str(leeftijd) + ' jaar')
SyntaxError: invalid syntax
>>> 
>>> if leeftijd < 18:hoelang_tot18jaar = 18 - leeftijd						print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')		elif leeftijd > 18:									hoelang_al18jaar = leeftijd - 18 						print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')		else:													    print('Het is alweer ' + str(leeftijd) + ' jaar')
SyntaxError: invalid syntax
>>> if leeftijd < 18:																					hoelang_tot18jaar = 18 - leeftijd																		print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')														    elif leeftijd > 18:																					hoelang_al18jaar = leeftijd - 18 																		print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')			    								    else:													    									print('Het is alweer ' + str(leeftijd) + ' jaar')
SyntaxError: invalid syntax
>>> 
>>> if leeftijd < 18:
    hoelang_tot18jaar = 18 - leeftijd
    print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
elif leeftijd > 18:
    hoelang_al18jaar = leeftijd - 18
    print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
else:
    print('Je bent precies ' + str(leeftijd) + ' jaar')

    
Over 1 jaar wordt je 18
>>> from random import randint
randint(0,1000)
willekeurig_getal = randint(0,1000)
willekeurig_getal
print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))

SyntaxError: multiple statements found while compiling a single statement
>>> from random import randint
>>> randint(0,1000)
894
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
13
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000: 13
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    datum.strftime('%A %d %B %Y')
NameError: name 'datum' is not defined
>>> datum.strftime('%A %d %B %Y')
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    datum.strftime('%A %d %B %Y')
NameError: name 'datum' is not defined
>>> import locale
>>> datum.strftime('%A %d %B %Y')
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    datum.strftime('%A %d %B %Y')
NameError: name 'datum' is not defined
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    datum.strftime('%A %d %B %Y')
NameError: name 'datum' is not defined
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
datum.strftime('%A %d %B %Y')
SyntaxError: multiple statements found while compiling a single statement
>>> from datetime import datetime
>>> datum = datetime.now()																			    print(datum)
    datum.strftime('%A %d %B %Y')
    
SyntaxError: invalid syntax
>>> datum = datetime.now()
>>> print(datum)
2020-09-18 15:25:50.784448
>>> datum.strftime('%A %d %B %Y')
'vrijdag 18 september 2020'
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
'vrijdag 18 september 2020'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> datum.strftime('%A %d %B %Y')
'venerdì 18 settembre 2020'
>>> 