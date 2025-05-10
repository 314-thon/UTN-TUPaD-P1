#trabajo práctico 4
"""
1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
"""
#usamos un bucle for para iterar desde 0 hasta 100
for i in range(101):
    #imprimimos el número actual
    print(i)


"""
2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
dígitos que contiene.
"""

#solicitamos al usuario un número entero
numero = input("Ingrese un número entero: ")
#verificamos si el número es negativo
if numero[0] == "-":
    #si es negativo, contamos los dígitos sin contar el signo
    cantidad_digitos = len(numero) - 1
else:
    #si es positivo, contamos los dígitos normalmente
    cantidad_digitos = len(numero)
#imprimimos la cantidad de dígitos
print(f"La cantidad de dígitos es: {cantidad_digitos}")

"""
3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
dados por el usuario, excluyendo esos dos valores.
"""

#solicitamos al usuario los dos valores
valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))
suma = 0
#verificamos que ambos valores no sean iguales
if valor1 == valor2:
    print("Los valores ingresados son iguales.")
else:
    if valor1 < valor2:
        #si es así, sumamos los números entre los dos valores
        for i in range(valor1 + 1, valor2):
            suma += i
    else:
        #si es al revés, invertimos los valores
        for i in range(valor2 + 1, valor1):
            suma += i
        #imprimimos la suma
    print(f"La suma de los números entre {valor1} y {valor2} es: {suma}")

"""
4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
un 0.
"""

#solicitamos al usuario un número entero para comenzar la suma
numero = int(input("Ingrese un número entero (0 para salir): "))
#inicializamos la variable suma en 0
suma = 0
#iniciamos un bucle que se repetirá mientras el número ingresado no sea 0
while numero != 0:
    #sumamos el número ingresado a la suma total
    suma += numero
    #solicitamos otro número al usuario
    numero = int(input("Ingrese un número entero (0 para salir): "))
#imprimimos la suma total
print(f"La suma total es: {suma}")

"""
5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
"""

import random
#generamos un número aleatorio entre 0 y 9
numero_aleatorio = random.randint(0, 9)
intentos = 0
numero_usuario = -1  #inicializamos el número del usuario

while numero_usuario != numero_aleatorio:
    numero_usuario = int(input("Adivina un número entre 0 y 9: "))
    intentos += 1
    if numero_usuario == numero_aleatorio:
        print(f"¡Felicidades! Adivinaste el número {numero_aleatorio} en {intentos} intentos.")
    else:
        print("Intenta de nuevo.")


"""
6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
entre 0 y 100, en orden decreciente.
"""



"""
7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
número entero positivo indicado por el usuario.
"""



"""
8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
menor, pero debe estar preparado para procesar 100 números con un solo cambio).
"""



"""
9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
poder procesar 100 números cambiando solo un valor).
"""



"""
10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
"""


