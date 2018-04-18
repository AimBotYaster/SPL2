 # regen.py
eingabe = input ("Hast du einen Regenschrim")
if(eingabe == "nein"):
            regen = True
            while (regen) :
                print ("warten bis der Regen aufhört")
                eingabe = input("regnet es noch?")
                if(eingabe == "nein"):
                    regen = False
                    print("es hat aufgehört zu regnen...")
                    break
                
                else :
                    print("es regnet noch immer...")
print ("geh nach draußen")

