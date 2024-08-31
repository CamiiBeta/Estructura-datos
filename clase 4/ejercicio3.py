#Verificar si una palabra es palabra dada es palindroma

palabra = str(input("Introduce la palabra que deseas saber si es palindroma:"))
palabra = list(palabra)
palabraInversa = []
for i in reversed(palabra):
    palabraInversa.append (i)
if palabra == palabraInversa:
    print("La palabra", palabra, "es palindroma")
else:
    print("La palabra", palabra, " no es palindroma")
