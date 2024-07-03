#def decoreer(tekst=""): 
 #   lengte = len(tekst) + 4
  #  print()
   # print(lengte * "*")
    #print(f"* {tekst} *")
    #print(lengte * "*")
    #print()


#def fooi_pp(bedrag, personen):
 #   bedrag_pp = bedrag / personen
  #  uitvoer = (f"het bedrag per person is {bedrag_pp} euro")

   # return uitvoer
#b = int(input("Welk bedrag zit er in de fooienpot? "))
#p = int(input("Over hoeveel mensen moet de pot verdeeld worden? "))

#print(fooi_pp(b,p))


#def fooi_pp(bedrag, person):
#    try:
#        bedrag_pp = bedrag / person
#    except:
#        bedrag_pp = "??"
 #       return f"het bedrag per persoon is {bedrag_pp} euro"
    
 #   b = int(input("welke bedrag zit er in de fooienpot? "))
  #  p = int(input("over hoeveel mensen moet de pot verdeeld worden? "))

    #print(fooi_pp(b, p))
#p = int(input("Over hoeveel mensen moet de pot verdeeld worden? "))


#def onderstreep(tekst = ""):
 #   uit = []
  #  uit.append(tekst)
   # uit.append(len(tekst) * "=")
    #return uit


def som(inkomsten_dict):
    return sum(inkomsten_dict.values())
