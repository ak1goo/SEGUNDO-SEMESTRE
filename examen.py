#PARTE I
#1 Lista
nombres = ["Ana", "Luis", "Pedro"]

#2 Para eliminar un elemento de una lista en Python, 
# se pueden utilizar varios métodos, entre ellos remove(), pop() y la palabra clave del. 
# Cada uno tiene su propia forma de funcionar y se adapta a diferentes necesidades. 

#3 
while True:
    print("Hola")
    break
#Imprime el texto "Hola"

#4 
diccionario=  {"Nombre:" "Heidelle Legrand", 
               "Edad: " "18", 
               "Carrera:" 
               "Ingenieria en Sistemas"
               }

#5
#Una tupla es inmutable, no se puede cambiar, mientras la lista si.

#PARTE II
#1 
suma = 0

while True:
    numeros = int(input("Ingrese un número: "))
    
    if numeros == 0:
        print(f"La suma es {suma}")
        break
        
    suma += numeros

#2
numeros = [10,20,30,40]
for numero in numeros:
    print(numero * 2)

#3
productos = [
    {"nombre": "Manzana", "precio": 3.5, "stock": 50},
    {"nombre": "Pan", "precio": 2.0, "stock": 100},
    {"nombre": "Jugo", "precio": 5.25, "stock": 30}
]

for producto in productos:
    print(f"El producto {producto['nombre']} cuesta Q{producto['precio']} y hay {producto['stock']} unidades disponibles.")


