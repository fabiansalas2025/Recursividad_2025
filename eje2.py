#Importar librerías
import os
#Limpia pantalla
os.system("cls")
#Defino función de la serie de Fibonacci
def fibonacci(n):
    #Calcula el valor de Fibonacci en la posición n usando recursividad.
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Solicita al usuario una posición límite
dato = int(input("Ingrese una posición (entero no negativo): "))

print(f"\nSerie de Fibonacci hasta la posición {dato}:\n")

#Muestra la serie completa
for i in range(dato + 1):
    print(f"F({i}) = {fibonacci(i)}")
