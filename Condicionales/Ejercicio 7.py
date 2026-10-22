renta = int(input("Introduce tu renta anual: "))
if renta < 10000:
    print("El tipo impositivo que te corresponde es del 5%")
elif renta <= 20000:
    print("El tipo impositivo que te corresponde es del 15%")
elif renta <= 35000:
    print("El tipo impositivo que te corresponde es del 20%")
elif renta <= 60000:
    print("El tipo impositivo que te corresponde es del 30%")
else:
    print("El tipo impositivo que te corresponde es del 40%") 
