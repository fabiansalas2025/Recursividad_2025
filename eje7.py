#Importar librerías
import os
#Limpia pantalla
os.system("cls")
#Defino función precursiva
def contar_bloques(n):
    #Devuelve el total de bloques necesarios para construir la pirámide.
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1) 
#Cantidad de bloques en la base
dato = int(input("Ingrese la cantidad de bloques en la base :"))
#Resultado por pantalla
print(f"Si colocas {dato} bloques en la base, necesitarás {contar_bloques(dato)} en total para terminar la pirámide")