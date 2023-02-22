# Pedir al usuario la edad y la altura
edad = int(input("Ingrese su edad: "))
altura = float(input("Ingrese su altura en metros: "))

# Verificar si la persona puede o no subirse a la montaña rusa "Push-Pull"
if edad >= 14 and altura >= 1.62:
    print("¡Felicitaciones! Puede subirse a la montaña rusa Push-Pull.")
else:
    if edad < 14 and altura < 1.62:
        print("Lo siento, no puede subirse a la montaña rusa Push-Pull porque es demasiado joven y demasiado pequeño/a.")
    elif edad < 14:
        print("Lo siento, no puede subirse a la montaña rusa Push-Pull porque es demasiado joven.")
    else:
        print("Lo siento, no puede subirse a la montaña rusa Push-Pull porque es demasiado pequeño/a.")
