edad = input("¿cuantos años tines?")

if (int(edad) >= 18) :
    print("Eres mayor de edad")
else:
    print ("Eres menor de edad")
print("-------------------")

numero_inical=2
numero_final=8
for i in range(numero_inical,numero_final):
    if (i%2!=0):
        print(i)
print("-------------------")

for i in range(100,0,-1):
    print(i)