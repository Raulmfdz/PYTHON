nombre = input("introduce tu nombre: ")
puntuacion = float(input("Introduce tu puntuacion obtenida (0.0, 0.4, 0.6 o más): "))

if puntuacion == 0.0:
    print("El usuario", nombre, "ha recibido una puntuación de", puntuacion, "y va a cobrar 2.400 euros.")
elif puntuacion == 0.4:
    print("El usuario", nombre, "ha recibido una puntuación de", puntuacion, "y va a cobrar 4.800 euros.")
elif puntuacion >= 0.6:
    print("El usuario", nombre, "ha recibido una puntuación de", puntuacion, "y va a cobrar 7.200 euros.")
else:
    print("Error: Puntuación no válida")