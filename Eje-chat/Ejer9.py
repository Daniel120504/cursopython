B_vendidas = int(input("Barras vendidas que no son del dia: "))

precio = 3.49 
descuento = 0.6
coste = B_vendidas * precio * (1 - descuento)

#str() se utiliza para convertir la variable precio a una cadena de texto (string).
print("El coste de una barra fresca es " + str(precio) + "€") #
print("El descuento sobre una barra no fresca es " + str(descuento * 100) + "%")
print("El coste final a pagar es " + str(round(coste, 2)) + "€")

