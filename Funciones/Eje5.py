def factorial(n): 
    
    resultado = 1
    for i in range(n): 
        resultado *=  i+1
    return resultado
        
print(factorial(5))