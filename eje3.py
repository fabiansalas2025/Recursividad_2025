#Importar librerías
import os
#Limpia pantalla
os.system("cls")
#Defino función potencia
def potencia(base, exponente):
    #Calcula la potencia de 'base' elevada a 'exponente' de forma recursiva
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# Ingreso base y exponente
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente (entero no negativo): "))
#Muestra por pantalla el resultado
resultado = potencia(base, exponente)
print(f"\n{base}^{exponente} = {resultado}")
