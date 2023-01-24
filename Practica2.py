numero_1=int(input('ingresar un Primer valor:'))
numero_2=int(input('ingresar un Segundo valor:'))


eleccion=int(input('Indique la Operaccion:'))

eleccion !=4

#1)Suma
#2)Resta
#3)Multiplicacion
#4)Division

if eleccion ==1:
    print(numero_1+numero_2)

if eleccion ==2:
    print(numero_1-numero_2)

if eleccion ==3:
    print(numero_1*numero_2)

if eleccion ==4:
    if numero_2==0:
        print('Indefinido')
    else:
        print(float(numero_1/numero_2))
