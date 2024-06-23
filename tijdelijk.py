from algemene_functie import mijn_functie_2

from helper import decoreer

def print_aanbieding():
    prijzen = {
        "aardbei": 3,
        "vanilla": 4,
        "chocolade": 5,
    }
  
    aanbieding = prijzen["aardbei"] * 0.8

    reclama_tekst = f"Vandaag in de aanbieding: aardbei-ijs, 1 liter - slechts €{aanbieding:2f}"

    reclama_tekst2 = reclama_tekst[:-4]

    reclama_tekst3 = reclama_tekst2.upper()

    reclama_tekst4 = reclama_tekst3.split()

    for el in reclama_tekst4:
        if len(el) <= 5:
            print(el.upper())
        else:
            print(el.lower())

decoreer("aanbieding")
mijn_functie_2("aanbieding")
print_aanbieding()
