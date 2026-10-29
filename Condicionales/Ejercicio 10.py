tipo = input("¿Quieres una pizza vegetariana? (si/no): ").lower()
if tipo == "si":
    print("Ingredientes disponibles: 1. Pimiento, 2. Tofu")
    eleccion = input("Elige el número de tu ingrediente (1 o 2): ")
    if eleccion == "1":
        ingrediente = "Pimiento"
    else:
        ingrediente = "Tofu"
    print("Pizza Vegetariana")
    print("Lleva: Mozzarella, tomate y", ingrediente)
else:
    print("Ingredientes disponibles: 1. Peperoni, 2. Jamón, 3. Salmón")
    eleccion = input("Elige el número de tu ingrediente (1, 2 o 3): ")
    
    if eleccion == "1":
        ingrediente = "Peperoni"
    elif eleccion == "2":
        ingrediente = "Jamón"
    else:
        ingrediente = "Salmón" 
    print("Pizza No Vegetariana")
    print("Lleva: Mozzarella, tomate y", ingrediente)