#sumar 2 matrices 2x2
matrizA= [[1,2],[3,4]]
matrizB= [[5,6],[7,8]]
matrizC= [[0,0],[0,0]]

for i in range(2):
    for j in range(2):
        matrizC[i][j]= matrizA[i][j] + matrizB[i][j]
        print(matrizC[i][j], end="  ")
    print()