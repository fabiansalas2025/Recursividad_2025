#Importar librerías
import os
#Limpia pantalla
os.system("cls")
#Defino función precursiva
def es_palindromo(palabra):
    #Verifica recursivamente si una palabra es un palíndromo.
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# Ingreso texto de prueba
texto = input("Ingrese una palabra sin espacios ni tildes: ").lower()

#Muestro por pantalla los resultados
if es_palindromo(texto):
    print(f'"{texto}" es un palíndromo.')
else:
    print(f'"{texto}" no es un palíndromo.')
