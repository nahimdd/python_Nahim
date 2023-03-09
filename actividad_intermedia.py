cursos = {}

def crear_curso(nombre, alumnos, estado, clases):
    cursos[nombre] = {"alumnos": alumnos, "estado": estado, "clases": clases}

def dar_de_alta_curso(nombre):
    cursos[nombre]["estado"] = "Activo"

def buscar_curso(nombre):
    if nombre in cursos:
        return cursos[nombre]
    else:
        return None

def mostrar_todos_los_cursos():
    for nombre, curso in cursos.items():
        print(nombre)
        print("  Alumnos:", curso["alumnos"])
        print("  Estado:", curso["estado"])
        print("  Clases:", curso["clases"])

def mostrar_informacion_del_curso(nombre):
    curso = buscar_curso(nombre)
    if curso:
        print("Curso:", nombre)
        print("  Alumnos:", curso["alumnos"])
        print("  Estado:", curso["estado"])
        print("  Clases:", curso["clases"])
    else:
        print("El curso", nombre, "no existe")


# Crear un curso:
crear_curso("Curso de QA Minds", 18, "No Iniciado", 25)

# Dar de alta un curso:
dar_de_alta_curso("Curso de QA Minds")

# Buscar curso, modificar estado:
curso = buscar_curso("Curso de QA Minds")
if curso:
    curso["estado"] = "Finalizado"
else:
    print("El curso no existe")

# Mostrar todos los cursos:
mostrar_todos_los_cursos()

# Informacion de un curso especifico:
mostrar_informacion_del_curso("Curso de QA Minds")

