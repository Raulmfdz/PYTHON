nombre = input("Introduce tu nombre: ")
sexo = input("Introduce tu sexo (m o f): ")
nom = nombre.lower()[0]
sex = sexo.lower()
if nom < "m" and sex == "f": 
    print ("Eres del grupo a")
elif nom >= "m" and sex == "f" :
    print ("Eres del grupo b")
elif nom > "n" and sex == "m" :
    print ("Eres del grupo a")
elif nom <= "n" and sex == "m" :
    print ("Eres del grupo b")
else :
    print ("Error")
