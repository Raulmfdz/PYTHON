CantidadInversion = float(input("Ingrese la cantidad de inversión: "))
InteresAnual = float(input("Ingrese el interés anual (en porcentaje): "))
Años = int(input("Ingrese la cantidad de años: "))
print("el capital obtenido es de ", CantidadInversion * (1 + (InteresAnual / 100) * Años))