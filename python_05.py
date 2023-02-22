# Pedir al usuario dos variables
a = int(input('Escriba el primer número 12: '))
b = int(input('Escriba el segundo número 34: '))

# Funciones para calcular la suma, resta, multiplicación, división y el módulo
def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def division(x, y):
    return x / y

def modulo(x, y):
    return y % x

# Imprimir resultados
print("La suma de a y b es:", suma(a, b))
print("La resta de a y b es:", resta(a, b))
print("La multiplicación de a y b es:", multiplicacion(a, b))
print("La división de a y b es:", division(a, b))
print("El módulo de b entre a es:", modulo(a, b))

print(80 * "-")

# Función para convertir cualquier número entero y a flotante
def convertir_numero(numero):
    return float(numero)

# Pedir al usuario un número para convertir
numero_usuario = input("Ingrese un número para convertir: ")
print("El número convertido es:", convertir_numero(numero_usuario))

print(80 * "-")

# Función para convertir de grados Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Pedir al usuario una temperatura en Celsius para convertir a Fahrenheit
temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
print("La temperatura en grados Fahrenheit es:", temperatura_fahrenheit)

print(80 * "-")

# Definir la función "es_par"
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

# Pedir al usuario que ingrese un número entero
numero_usuario = int(input("Ingrese un número entero: "))

# Utilizar la función "es_par" para determinar si el número es par o impar
if es_par(numero_usuario):
    print(numero_usuario, "es un número par.")
else:
    print(numero_usuario, "es un número impar.")

