#Importar librerías
import os
#Limpia pantalla
os.system("cls")
#Defino función precursiva
def contar_digito(numero, digito):
    #Cuenta recursivamente cuántas veces aparece un dígito en un número.
    if numero == 0:
        return 0
    else:
        ultimo = numero % 10
        if ultimo == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)
#Datos ingresados 
dato1= int(input("Ingrese un número cualquiera : "))
dato2= int(input("Ingrese el digito que quiere encontrar: "))
#Resultados mostrados por pantalla
print(f"El núemro ingresado es {dato1} el número {dato2}, fue encontrado {contar_digito(dato1, dato2)} veces")