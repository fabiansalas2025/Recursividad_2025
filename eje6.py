#Importar librerías
import os
#Limpia pantalla
os.system("cls")
#Defino función precursiva
def suma_digitos(n):
    #Calcula recursivamente la suma de los dígitos de un número entero positivo.
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)
#Ingreso número positivo por consola        
dato = int(input("Ingrese un número :"))
#Muestro resultado por pantalla
print(f"La suma de los digitos del número {dato} es {suma_digitos(dato)}.")