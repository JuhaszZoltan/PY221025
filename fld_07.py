a:int = int(input('derékszögű 3szög egyik befogója (cm): '))
b:int = int(input('derékszögű 3szög másik befogója (cm): '))
c = (a ** 2 + b ** 2) ** .5

print(f'a háromszög átfogója: {c} cm')