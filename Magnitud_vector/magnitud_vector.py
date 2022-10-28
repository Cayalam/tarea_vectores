# Calcular la magnitud de un vector
print("..................................................")
print(".....Calculador...de...magnitudes...vectorial.....")
print("..................................................")

x1=int(input("Ingresa la primera cordenada en la posiciòn X: "))
y1=int(input("Ingresa la primera cordenada en la posiciòn Y: "))
x2=int(input("Ingresa la segunda cordenada en la posiciòn X: "))
y2=int(input("Ingresa la segunda cordenada en la posiciòn Y: "))

# procecing
from  math import sqrt
r=sqrt((x2-x1)**2 + (y2-y1)**2)


print("La magnitud vectoriañ es: ",r)
