# Trabajo práctico 5
"""
1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
range.
"""

lista_multiplo_4 = []
for i in range(1, 101):
    if i % 4 == 0:
        lista_multiplo_4.append(i)
print("Los números del 1 al 100 que son múltiplos de 4 son:", lista_multiplo_4)

"""
2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
indexing con números negativos!
"""

personajes_valorant = ["Phoenix", "Jett", "Sova", "Cypher", "Killjoy"]
print("El penúltimo personaje de la lista es:", personajes_valorant[-2])

"""
3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
ejemplo:
lista_vacia = []
"""

lista= []
lista.append("pichichos")
lista.append("michis")
lista.append("negritos")
print("La lista resultante es:", lista)

"""
4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
en los videos o bien investigar cómo funciona el indexing con números negativos!
animales = ["perro", "gato", "conejo", "pez"]
"""

animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print("La lista resultante es:", animales)

"""
5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))  
print(numeros)
"""

#respuesta: Elimina el número mayor de la lista "numeros" y luego imprime la lista resultante sin ese número.
#en este caso, el número mayor es 22, por lo que la lista resultante será [8, 15, 3, 7].
#pero también funciona con floats y strings por ejemplo, pero todos los elementos de la lista deben ser del mismo tipo.
#----------------------------------------------------------------------------------------

"""
6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
pantalla los dos primeros.
"""
lista = []
for i in range(10, 31, 5):
    lista.append(i)
print("Los dos primeros números de la lista son:", lista[:2])


"""
7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]
"""
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "focus"
autos[2] = "fit"
print("La lista resultante es:", autos)


"""
8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
directamente. Imprimir la lista resultante por pantalla.
"""

lista = []
lista.append(5*2)
lista.append(10*2)
lista.append(15*2)
print("La lista resultante es:", lista)

"""
9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]
a) Agregar "jugo" a la lista del tercer cliente usando append.
b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
c) Eliminar "pan" de la lista del primer cliente.
d) Imprimir la lista resultante por pantalla
"""



"""
10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
● Posición lista_anidada[0]: 15
● Posición lista_anidada[1]: True
● Posición lista_anidada[2][0]: 25.5
● Posición lista_anidada[2][1]: 57.9
● Posición lista_anidada[2][2]: 30.6
● Posición lista_anidada[3]: False
Imprimir la lista resultante por pantalla.
"""



#----------------------------------------------------------------------------------------
#Fin del trabajo práctico