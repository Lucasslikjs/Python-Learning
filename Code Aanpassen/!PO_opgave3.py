#while-loop naar for-loop


#while-loop
#x = 1
#saldo = 0
#while x < 10000:
    #saldo = saldo + x
    #x = x + 1
#print(saldo)

#for-loop
saldo = 0
for x in range(10000):
  saldo += x
print(saldo)