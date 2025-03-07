a = int(input("Ingrese un numero A: "))
b = int(input("Ingrese un numero B: "))
c = int(input("Ingrese un numero C: "))

if a > b and a > c:
    print( a, " es el numero es mayor")
elif b > a and b > c:
    print( b, " es el numero es mayor")
elif c > a and c > b:
    print( c, " es el numero es mayor")

else:
    print( "Todos son iguales")
