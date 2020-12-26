aantalGetallen = int(input("Hoeveel getallen wil je invoeren?"))
totaal = 0 
teller = 0 

while teller < aantalGetallen: 
    getal = float(input("Voer getal in")) 
    totaal += getal 
    teller += 1 
    
    gemiddelde = totaal / aantalGetallen "
    print("Het gemiddelde is: " + str(gemiddelde)) 



