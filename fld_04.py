arfolyam = float(input('€ árfolyama: '))
forint = int(input('ennyi HUF-od van: '))
euro:float = round(forint / arfolyam, 2)

print(f'ez ennyit ér: {euro}€')