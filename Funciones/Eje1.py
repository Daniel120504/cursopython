#Conociendo funciones en python
def mi_funcion(num1,num2):
    
    resultado = num1 + num2
    print(resultado)
    
    if resultado > 100:
        print("El numero es mayor que 100")
    else: 
        print("El numero es menor que 100")

mi_funcion(23,89)


def saludos(nombre): 
    
    print(f"Hola{nombre}")
nombre_persona = input("Ingresa tu nombre: ")
saludos(nombre_persona)

