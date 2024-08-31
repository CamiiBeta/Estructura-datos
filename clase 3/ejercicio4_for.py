#factorial de un numero

factorial=int(input("Ingresa el número que deseas sacarle factorial:"))
resultado=1
for i in range(1, factorial+1):
    resultado = resultado*i 
print ("El factorial de", factorial, "es", resultado)