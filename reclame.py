
def meervoudig(invoer_lijst):
    laagste = min(invoer_lijst)
    hoogste = max(invoer_lijst)
    return [laagste, hoogste]

invoer_lijst = [10, 5, 3, 2, 1, 2, 9]
resultaat_meervoudig = meervoudig(invoer_lijst)
print(resultaat_meervoudig) 



def meervoudig(invoer_lijst):
    return [item * 2 for item in invoer_lijst]

def mijn_functie_2(korte_lijst):
    return sum(korte_lijst)

def combinatie(invoer_lijst_2):
    korte_lijst = meervoudig(invoer_lijst_2)
    resultaat = mijn_functie_2(korte_lijst)
    return resultaat

voorbeeld_lijst = [1, 2, 3, 4]
resultaat = combinatie(voorbeeld_lijst)
print(resultaat)
