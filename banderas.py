flag = False
num = int(input("Ingrese un número: "))

if num % 2 == 0:
    flag = True

if flag:
    print("El número ingresado es un número par")
else:
    print("El número ingresado no es un número par")