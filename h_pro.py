from helper import onderstreep

uitvoer = onderstreep("aanbieding")
uitvoer.append("aardbijenijs emmer van 5 liter: 5 euro")
uitvoer.append("salgroom, spuitbus van 1 liter: 2 euro")

print()

for el in uitvoer:
    print(el)