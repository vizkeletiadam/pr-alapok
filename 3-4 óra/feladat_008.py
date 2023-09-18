"""
kérjünk be egy jegyet 1-5és irassuk ki a megadott jegy értékét számmal és szöveggel.
"""

jegy = int(input("kérek egy jegyet 1-5 : "))
if jegy ==5:
    print('a jegyed {jegy}jeles. jeles' )
if jegy ==4:
    print('a jegyed {jegy}jeles. jó' )
if jegy ==3:
    print('a jegyed {jegy}jeles. közepes' )
if jegy ==2:
    print('a jegyed {jegy}jeles. elégséges' )
if jegy ==1:
    print('a jegyed {jegy}jeles. elégtelen' )