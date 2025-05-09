#ejercicio 1
# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
#solicitamos la edad al usuario

edad = int(input("Ingrese su edad: "))
#verificamos si es mayor de edad
print("Es mayor de edad") if edad >= 18 else print("Es menor de edad")

#----------------------------------------------------------------------------------------

#ejercicio 2
# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

#solicitamos la nota al usuario
nota = int(input("Ingrese su nota: "))
#verificamos si es mayor o igual a 6
print("Aprobado") if nota >= 6 else print("Desaprobado")

#----------------------------------------------------------------------------------------

#ejercicio 3
# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

#solicitamos el numero al usuario
numero = int(input("Ingrese un numero: "))
print("Ha ingresado un numero par") if numero % 2 == 0 else print("Por favor, ingrese un numero par")

#----------------------------------------------------------------------------------------

#ejercicio 4
# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años.

#solicitamos la edad al usuario
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#----------------------------------------------------------------------------------------

#ejercicio 5
# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

#solicitamos la contraseña al usuario
password = input("Ingrese su contraseña: ")
#verificamos si la longitud es correcta
if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#----------------------------------------------------------------------------------------

#ejercicio 6
# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
# y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el
# siguiente:
## from statistics import mode, median, mean
## mi_lista = [1,2,5,5,3]
## mean(mi_lista)
# En la documentación oficial se puede encontrar más información sobre este paquete:
# https://docs.python.org/es/3.8/library/statistics.html.
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
# mediana es mayor que la moda.
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
# la mediana es menor que la moda.
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma:
## import random
## numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
# forma aleatoria.

from statistics import mode, median, mean
import random
# Definimos la lista numeros_aleatorios
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# Calculamos la moda, mediana y media
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
# Imprimimos los resultados
print("Lista de números aleatorios: ", numeros_aleatorios)
print("Moda: ", moda)
print("Mediana: ", mediana)
print("Media: ", media)
# Comparamos los resultados para determinar el sesgo
if media > mediana > moda:
    print("Sesgo positivo")
elif media < mediana < moda:
    print("Sesgo negativo")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("No se puede determinar un sesgo claro")

#----------------------------------------------------------------------------------------

#ejercicio 7
# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

#solicitamos la frase al usuario
frase = input("Ingrese una frase o palabra: ")
#verificamos si termina con vocal
print(frase + "!") if frase[-1].lower() in "aeiou" else print(frase)

#----------------------------------------------------------------------------------------

#ejercicio 8
# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

#solicitamos el nombre al usuario
nombre = input("Ingrese su nombre: ")
#solicitamos la opcion al usuario
opcion = int(input("Ingrese 1 para mayusculas, 2 para minusculas o 3 para capitalizar: "))
#verificamos la opcion elegida
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opcion no valida. Debe ingresar 1, 2 o 3.")

#----------------------------------------------------------------------------------------

#ejercicio 9
# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

#solicitamos la magnitud al usuario
magnitud = float(input("Ingrese la magnitud del terremoto: "))
#verificamos la magnitud
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
elif magnitud >= 7:
    print("Extremo (puede causar graves daños a gran escala)")
else:
    print("Magnitud no valida. Debe ingresar un numero.")

#----------------------------------------------------------------------------------------

#ejercicio 10
# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
# Periodo del año | Estación en el hemisferio norte |Estación en el hemisferio sur
# (21-12 a 20-03) | Invierno                        | Verano
# (21-03 a 20-06) | Primavera                       | Otoño
# (21-06 a 20-09) | Verano                          | Invierno
# (21-09 a 20-12) | Otoño                           | Primavera

# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

# Pedimos y validamos el mes
mes = int(input("Ingrese el mes (1-12): "))
if mes < 1 or mes > 12:
    print("Mes inválido. Debe estar entre 1 y 12.")
else:
    # Pedimos y validamos el día
    dia = int(input("Ingrese el día (1-31): "))
    if dia < 1 or dia > 31:
        print("Día inválido. Debe estar entre 1 y 31.")
    else:
        # Determinamos el rango estacional 
        if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
            estacion_norte = "Invierno"
            estacion_sur = "Verano"
        elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
            estacion_norte = "Primavera"
            estacion_sur = "Otoño"
        elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
            estacion_norte = "Verano"
            estacion_sur = "Invierno"
        elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
            estacion_norte = "Otoño"
            estacion_sur = "Primavera"
        else:
            print("Fecha fuera de rango para determinar estación.")

# Ahora pedimos y validamos el hemisferio
hemisferio = input("Ingrese su hemisferio (N/S): ").upper()
if hemisferio == "N":
    print(estacion_norte)
elif hemisferio == "S":
    print(estacion_sur)
else:
    print("Hemisferio no válido. Debe ingresar N o S.")

#----------------------------------------------------------------------------------------
#Fin del trabajo práctico