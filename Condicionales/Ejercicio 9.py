Edad = int(input ("Introduce tu edad: "))
if Edad < 4 :
    print (F"Entra gratis ya que tiene {Edad} años")
elif Edad < 18 :
    print (F"Tienes que pagar 5 euros ya que tiene {Edad} años")
elif Edad >= 18 :
    print (F"Tienes que pagar 10 euros ya que tiene {Edad} años")
else :
    print ("Edad no valida")
 