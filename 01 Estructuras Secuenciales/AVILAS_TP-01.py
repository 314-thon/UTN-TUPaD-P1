#Actividades 
 
#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.  

print ("Ejercicio 1")
print("Hola Mundo!")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
# realizar la impresión por pantalla. 

print("")
print ("Ejercicio 2")
nombre = input("Ingrese un nombre: ")
print(f"Su nombre es: {nombre}")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
# la impresión por pantalla. 

print("")
print ("Ejercicio 3")
nombre = input("Ingrese un nombre: ")
apellido = input("Ingrese un apellido: ")
edad = input("Ingrese un edad: ")
lugar = input("Ingrese lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}.")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
# su perímetro. 

print("")
print ("Ejercicio 4")
radio = int(input("Digite el radio del círculo: "))

pi = 3.1416
area = pi * radio ** 2
perimetro = 2 * pi * radio

print(f"el área de su círculo es {area} y el perímetro es {perimetro}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
# cuántas horas equivale. 

print("")
print ("Ejercicio 5")
segundos = int(input("Digite la cantidad de segundos a calcular: "))
hora = (segundos // 60) // 60
print(f"Los segundos ingresados {segundos}, equivalen a {hora} horas.")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
# multiplicar de dicho número.  

print("")
print ("Ejercicio 6")
numero=int(input("Escriba un número para saber su tabla de multiplicar."))
print(f"1*{numero} =", 1*numero)
print(f"2*{numero} =", 2*numero)
print(f"3*{numero} =", 3*numero)
print(f"4*{numero} =", 4*numero)
print(f"5*{numero} =", 5*numero)
print(f"6*{numero} =", 6*numero)
print(f"7*{numero} =", 7*numero)
print(f"8*{numero} =", 8*numero)
print(f"9*{numero} =", 9*numero)

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 

print("")
print ("Ejercicio 7")
print("Ingrese dos números enteros distintos del 0 para calcular el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.")
num1=int(input("Escriba el primer número."))
num2=int(input("Escriba el segundo número."))
print(f"{num1}+{num2}=", num1+num2)
print(f"{num1}/{num2}=", num1/num2)
print(f"{num1}*{num2}=", num1*num2)
print(f"{num1}-{num2}=", num1-num2)



#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente 
# modo:  
# 𝐼𝑀 𝐶  =   𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔
# (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚 ) 2

print("")
print ("Ejercicio 8")
print("Para calcular su IMC se necesitan los siguientes datos:")
altura=float(input("Ingrese su altura en metros (ej: 1.85): "))
peso=float(input("Ingrese su peso en kg (ej: 80): "))
IMC=peso/(altura**2)
print(f"Su IMC es de: {IMC}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 
# 𝑇𝑒𝑚 𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡  = 95 . 𝑇𝑒𝑚 𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠    +  32

print("")
print ("Ejercicio 9")
tempC=float(input("Ingrese la temperatura en Celsius: "))
tempF=(tempC*9/5)+32
print(f"{tempC}° Celsius equivalen a {tempF}° Fahrenheit.")

#10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
# dichos números. 

print("")
print ("Ejercicio 10")
print("Ingrese 3 números para calcular el promedio.")
num1=float(input("Ingrese el primer número: "))
num2=float(input("Ingrese el segundo número: "))
num3=float(input("Ingrese el tercer número: "))
promedio=(num1+num2+num3)/3
print(f"el promedio de {num1}, {num2} y {num3} es de {promedio}.")