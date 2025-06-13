#Importar librerías
import os
#Limpia pantalla
os.system("cls")
#Defino función factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)   
# Ingreso de dato
dato = int(input("Ingrese un número :"))

for i in range(1, dato + 1):
    print(f"{i}! = {factorial(i)}")

#Imprime por pantalla el resultado final

print(f"el factorial de {dato} es {factorial(dato)}")