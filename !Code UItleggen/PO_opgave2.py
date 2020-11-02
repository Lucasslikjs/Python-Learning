aantalGetallen = int(input("Hoeveel getallen wil je invoeren?")) #Er word gevraagd hoeveel getal de gebruiker wil invoeren
                                                                 #Door middel van de funtie "input"
totaal = 0 #Deze regel maakt een variable aan genaamd "totaal"
teller = 0 #Deze regel maakt een variable aan genaamd "telles"

while teller < aantalGetallen: #Als de variable "teller" kleiner is dan "aantalGetalen" gebeurt het volgede:
    getal = float(input("Voer getal in")) #Vraag de gebruiken om een getal in te vullen
    totaal += getal #Voegt het getal toe aan de variable "totaal"  
    teller += 1 #Verhoog de variable "teller" met 1
    
    gemiddelde = totaal / aantalGetallen #Deelt de som "totaal" door "aantalGetallen"
    print("Het gemiddelde is: " + str(gemiddelde)) #laat het gemiddelde zien doormiddel van de functie print



#1. The program asks the user how many numbers are there (say n)
#2. The program sets temporary variables called teller and totaal to 0
#3. While teller is less than n, it does the following:
    # 1. Ask the user a number
    # 2. Add the number to totaal 
    #3. Increase the teller by 1
#4. Divide the sum (totaal) by n and print it
