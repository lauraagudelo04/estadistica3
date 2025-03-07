anio = int(input("Digite un año: "))

if anio % 100 != 0:
    if anio % 4 == 0:
        print('Año bisiesto')
    else:
        print('No bisiesto')

elif anio % 400 == 0:
    print('Año bisiesto')
else:
    print('No bisiesto')

