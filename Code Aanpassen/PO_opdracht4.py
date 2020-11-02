
#pin = int(input("Welkom!! Voer uw pincode in:"))
#if pin != 1234:
    #print("Fout! U mag het nog 2 keer proberen")
    #pin = int(input("Welkom!! Voer uw pincode in:"))
    #if pin != 1234:
        #print("Fout! U mag het nog 1 keer proberen")
        #pin = int(input("Welkom!! Voer uw pincode in:"))
        #if pin != 1234:
            #print("Fout! Uw pas is geblokkeerd!")
        #else:
            #print("Correcte pincode")
    #else:
         #print("Correcte pincode")
#else:
    #print("Correcte pincode")

#
#for-loop oplossing
#

for x in range(3):
    pin = int(input("Welkom!! Let op u heeft 3 kansen! Voer uw pincode in:"))
    if pin != 1234:
        print("Fout! Probeer het nog een keer!")
if pin != 1234:
    print("Fout! Uw pas is geblokkeerd!")
else:
    print("Correcte pincode")

