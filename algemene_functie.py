def mijn_functie_1(a):
    return a * a

print(mijn_functie_1(2))

def mijn_functie_2(a,b):
   uitvoer_lijst =  []
   uitvoer_lijst.append(a+b)
   uitvoer_lijst.append(a-b)
   uitvoer_lijst.append(a*b)
   uitvoer_lijst.append(a/b)
   return uitvoer_lijst
inkomen = mijn_functie_2("a","b")
resultaat = mijn_functie_1(inkomen)
print(resultaat)