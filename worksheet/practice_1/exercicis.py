import numpy as np


"""
Write a line of code that will print your name.
"""
print("Adrian")

"""How do you enter a comment in a program?"""

# Hay 2 tipos (#) o ('''text''')

"""What do the following lines of code output? ALSO: Why do they give a different answer?"""

# El primero divide, pero el de abajo saca el residuo 
print(2 / 3)
print(2 // 3)

"""
Write a line of code that creates a variable called pi and sets it to an appropriate value.
Why does this code not work?
"""
#Es case sensitive, significa que las variables son sensibles dependiendo si son en
#mayuscula o en minuscula

A = 22
print(a)

"""All of the variable names below can be used. But which ONE of these is the better variable name to use?"""
#Por el úso del snake case en python por convención

a
A
Area
AREA
area            <-
area_of_rectangle
Area_Of_Rectangle
"""
Which of these variables names are not allowed in Python? (More than one might be wrong. Also, this question is not asking about improper names, just names that aren't allowed. Test them if you aren't sure.)
"""
apple
Apple
APPLE
Apple2
1Apple          <-
account number
account_number
account.number
accountNumber
account#        <-
pi
PI
fred
Fred
GreatBigVariable
greatBigVariable
great_big_variable
great.big.variable
2x              <-
x2x
total%
#left           <-


"""Why does this code not work?"""
print(a)
a = 45

"""Explain the mistake in this code:"""
# Es una constante, se decalra la constante en mayusulas, luego no hace falta convertir el tipado en float, porque automaticamente detecta como un float al haber puesto el punto. Luego si es mucho mas largo puede detectarlo como un double, pero no se suele usar por optimización.
pi = float(3.14)

#Correct
PI = 3.14

"""This program runs, but the code still could be better. Explain what is wrong with the code."""
# La variable hace shadowing con otra variable, luego lo usa para hacer una operacion. Es inecesario el uso de otra variable, y como es una variable constante por convencion se dbee de poner mayusuclas y eitar reflejar en otra variable un mismo valor.
radius = float(input("Radius:"))
x = 3.14
pi = x
area = pi  * radius ** 2
print(area)

"""Explain the mistake in the following code:"""
#Multiplica "x" por "y", y lo imprime
x = 4
y = 5
a = ((x) * (y))
print(a)

"""Explain the mistake in the following code:"""
# El numero tren no realiza ninguna operacion que esta ubicada junto con el parentesis.
x = 4
y = 5
a = 3(x + y)
print(a)

"""Explain the mistake in the following code:"""
#Si queremos parsear el valor del input, necesitamos antes obtener el valor introudccido y luego parsearlo en float. Pero siempre usar un manejo de errores para eviatar errores inesperados.
radius = input(float("Enter the radius:"))

#Correct
radius = input("Enter the radius:")
print(float(radius))

"""Do all these print the same value? Which one is better to use and why?"""
# Sale los mismos resultados, es mejor el 2 por la legibilidad que tiene, ni es tan separado ni tan junto para poderse leer con facilidad
print(2/3+4)
print(2 / 3 + 4)
print(   2 /    3+    4  )

#yijan
"""What is a constant?"""
#Es una forma de guardar un valor de forma constante, sin poderse modificarse como las mismas variables.
#Se es escriben en mayucula y se usan con un = luego de añadir la variable.
# PI = 3.14
# print(f"{PI=}")

"""How are variable names for constants different than other variable names?"""
# Se esciben en mayusula

"""What is a single quote and what is a double quote? Give and label an example of both."""
# Comillas simples: ''
# Comilllas dobles: ""


""""Write a Python program that will use escape codes to print a double-quote and a new line using the Window's standard. (Note: I'm asking for the Window's standard here. Look it up out of Chapter 1.)"""
print("Esto es un escape con doble comillas: \"\"")

"""Can a Python program print text to the screen using single quotes instead of double quotes?"""
#Si

"""Why does this code not calculate the average?"""
#Porque por las reglas jerarquicacas de los operadores de prioridad, el divisor comienza el primero, y leugo suma de del resultado del la division del 5/3.
print(3 + 4 + 5 / 3)

#Correct
print((3 + 4 + 5) / 3)

#Better
array_avg = np.array([3, 4, 5])
avg = np.average(array_avg)

"""What is an ``operator'' in Python?"""

"""What does the following program print out?"""
#Imprimira un 4 (int)
x = 3
x + 1
print(x)

"""Correct the following code:"""

#Wrong
user_name = input("Enter your name: )"

#Correct
user_name = input("Enter your name: ")

"""Correct the following code:"""
#Wrong
value = int(input(print("Enter your age")))

#Correct
value = int(input("Enter your age"))