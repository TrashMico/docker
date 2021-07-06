import math
def desviacion_estandar(num):
    Fa=[]
    promedio=sum(num)/len(num)
    for i in range(len(num)):
        Fa.append(pow((num[i]-promedio),2))

    Fin=math.sqrt(sum(Fa)/len(Fa))
    print("La desviacion estandar es de ", Fin)
        
N =int(input("Ingrese la cantidad de numeros a evaluar "))
NL=[]

for i in range(N):
    NL.append(float(input("Ingrese el numero ")))
    print("Numero actuales ingresados: ",NL)
    

desviacion_estandar(NL)








    





