secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")
cont = 0
num = int(input("Ingresa el número entero: "))

while num != secret_number:
    print("Haz caido en el bucle. intentalo de nuevo")
    break
else:
    print("Lo lograste.")