#Sumar multiplos de 5
numero = 0
suma = 0

numero_maximo = int(input("Introduce el numero maximo: "))

while numero < numero_maximo:
    suma = suma + numero
    numero += 5

print("La suma es: ",suma)