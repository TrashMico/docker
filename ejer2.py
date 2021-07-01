canti=int(input("ingrese la cantidad de numeros a ingresar: "))
menor=float("inf")
mayor=-float("inf")

for i in range(canti):
    num=(float(input("ingrese un numero: ")))
    if num<menor:
        menor=num
    elif num>mayor:
        mayor=num
print("numero mayor: ",mayor, "numero menor: ",menor)