# Simple
from pickle import PROTO

a = 33
b = 200

if b > a:
    print (b, "Es mayor que ",a)

#Doble
y = 200
z = 333

if y > z:
    print(y, " es mayor que", z)
else:
    print(y, " no es mayor que ", z)

#Multiple
p = 200
d = 207

if p > d:
    print(p, " es mayor que ",d)
elif p < d:
    print(p," es menor que ", d)
else:
    print(p, "es igual que ", d)

#Enlazadas
x= 28
if x > 10:
    print("Por encima de diez, ")
    if x > 20:
     print("y tambien por encima de 20!")
    else:
        print("pero no por encima de 20.")

#Parametros end y sep
#end
print("Estudiar los sabados" , end=' ')
print("es genial")
#sep
print("Daniel", "Luis", "Carlos" , "Camila")  #Agrega un espacio por defecto
print("Daniel", "Luis", "Carlos" , "Camila", sep = "")  #Quitar el espacio
print("Daniel", "Luis", "Carlos" , "Camila", sep = ",")  #Agregar una coma

print("Daniel", "Luis", "Carlos" , "Camila" , sep = "_" , end = "_Curso_Python") #Inpñementacion end y set



