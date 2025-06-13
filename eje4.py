#Importar librerías
import os
#Limpia pantalla
os.system("cls")
#Defino función precursiva
def decimal_a_binario(n):
    #Convierte un número entero positivo a binario usando recursividad.
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Solicita al usuario un número entero positivo
numero = int(input("Ingrese un número entero positivo: "))

# Caso especial para el 0
if numero == 0:
    binario = "0"
else:
    binario = decimal_a_binario(numero)
#Muestra por pantalla el resultado
print(f"El número {numero} en binario es: {binario}")
