# crear una condicion donde los menores de 18 no puedan entrar
edad = int(input("Introduce tu edad: "))
if edad < 18:
    print("no puedes entrar")
else:
    print("puedes entrar")

# preguntar el nombre y mostrar en pantalla la edad y el nombre
nombre = input("¿Cuál es tu nombre?")
edad = int(input("¿Cuál es tu edad?"))
print("Hola", nombre, "tienes", edad, "años" )
