fila = int(input("Ingrese el numero de filas ==> "))
columna = int(input("Ingrese el numero de columnas ==> "))
matriz = []

for i in range (fila):
    matriz.append([])
    for j in range(columna):
        valor=int(input(f"Ingrese el valor {i} {j} de la matriz: "))
        matriz[i].append(valor)

for i in matriz:
    print(i)
    print() #imprime un espacio entre filas para que se observa