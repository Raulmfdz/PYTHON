peso = float(input("Ingrese su peso en kg: "))
Estatura = float(input("Ingrese su estatura en metros: "))
IMC = round(peso / (Estatura ** 2), 2)
print(f"Su indice de masa corporal es: {IMC}")