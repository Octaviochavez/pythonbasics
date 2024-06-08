suma = 0
num1 = int(input("Ingrese el primer número: "))
if num1 % 2 == 0:
    suma = suma + 1
num2 = int(input("Ingrese segundo número: "))
if num2 % 2 == 0:
    suma = suma + 1
num3 = int(input("Ingrese tercer número: "))
if num3 % 2 == 0:
    suma = suma + 1
print("La cantidad de números pares es " ,suma)