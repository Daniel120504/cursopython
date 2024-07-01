numero_entero = int(input("Dame un numero: "))

#Primer argumento: valor inicial inicial de la secuencia
#Segundo argumento: es el valor en el que la secuencia se detiene
#Tercer argumento: incremento entre cada valor de la secuencia 
#Ejemplo de funcionalidad: 
# 1 + 2 = 3 + 2 = 5 HASTA AQUI ES NUESTRO LIMITE nuestros numeros son = 1,3,5

for i in range(1, numero_entero+1 , 2): 
    print(i, end=", ")