print("Bereken het cijfer van je werkstuk")
inhoud = float(input("Deelcijfer voor de inhoud")) 
taalEnStijl = float(input("Deelcijfer voor taal en stijl"))
opmaak = float(input("Deelcijfer voor opmaak"))
cijfer = 0.6 * inhoud + 0.3 * taalEnStijl + 0.1 * opmaak 

if cijfer > 5.5:
    print("Je hebt een voldoende gehaald, een " + str(cijfer))
else: 
    print("Je hebt een onvoldoende gehaald, een " + str(cijfer))