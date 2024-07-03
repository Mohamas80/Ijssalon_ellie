

from helper import *
from presentatie import *


inkomsten = {
    'Aardbeien-ijs-totaal': 1000,
    'Vanille-ijs-totaal': 2000,
    'Chocolade-ijs-totaal': 1500,
    'Waterijsjes-totaal': 750
}

totaal_inkomsten = som(inkomsten)
print(f"de total inkomsten zijn: {totaal_inkomsten}")

presenteer(inkomsten, totaal_inkomsten)