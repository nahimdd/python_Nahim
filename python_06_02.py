# Importar la librería datetime
import datetime

# Pedir al usuario el día, mes y año de nacimiento
dia = int(input("Ingrese el día de su nacimiento (1-31): "))
mes = int(input("Ingrese el mes de su nacimiento (1-12): "))
anio = int(input("Ingrese el año de su nacimiento (ej. 1990): "))

# Calcular la edad
fecha_actual = datetime.datetime.now()
edad = fecha_actual.year - anio - ((fecha_actual.month, fecha_actual.day) < (mes, dia))

# Determinar si la persona ya cumplió años en lo que va del año
cumplio_anios = False
if fecha_actual.month > mes:
    cumplio_anios = True
elif fecha_actual.month == mes and fecha_actual.day >= dia:
    cumplio_anios = True

# Determinar a qué generación pertenece
if anio >= 1920 and anio <= 1939:
    generacion = "La generación silenciosa"
elif anio >= 1940 and anio <= 1959:
    generacion = "Los baby boomers"
elif anio >= 1960 and anio <= 1979:
    generacion = "La generación X"
elif anio >= 1980 and anio <= 1989:
    generacion = "La generación Y o millennials"
else:
    generacion = "La generación Z"

# Imprimir resultados
print("Usted tiene", edad, "años.")
if cumplio_anios:
    print("Ya cumplió años este año.")
else:
    print("Aún no ha cumplido años este año.")
print("Pertenece a:", generacion + ".")