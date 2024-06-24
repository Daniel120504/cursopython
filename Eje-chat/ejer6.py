#Suma de numeros pares 

num_inicial = int(input("Introduce el numero inicial: "))
num_final = int(input("Introduce el numero final: "))
cont  = 0

while num_inicial < num_final:
    if num_inicial % 2 == 0: 
        print(num_inicial)
        cont += 1
    num_inicial += 1
    
print("Hay", cont, "numeros pares")

