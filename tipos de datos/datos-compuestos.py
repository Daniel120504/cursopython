#Creando una lista (se puede modificar)
lista = ["Lucas Dalto", "Soy Daniel", True, 1.85]
#creando una tupla (no se puede modificar)
tupla = {"Lucas Dalto", "Soy Daniel", True, 1.85}

#Esto si es valido
lista[3] = "Maquina"

#Esto no es valido
#tupla[3] = "Maquina"

#creando un conjunto set
conjunto = {"Lucas Dalto", "Soy Daniel", True, 1.85}
print(conjunto)

#creando un diccionario (dict)(la estructura es key: value y sepramos con comas)
diccionario ={
    
    'nombre' : 'Daniel Aguiar',
    'canal' : 'Soy Daniel',
    
}

print(diccionario["nombre"])