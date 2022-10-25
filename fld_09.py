fogy = float(input('Mennyit eszik az autó 100-on? '))
ut = int(input('Hány Km-et akarunk utazni? '))
ar = int(input('Mennyibe kerül a benzin? '))

print(f'utiköltség: {ut * ar * fogy / 100} Ft')