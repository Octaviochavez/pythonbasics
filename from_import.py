from os import system
system("cls")
#Crear lista vacia
clientes= []
while True:
    system("cls")
    print("""
    1. Guardar cliente
    2. Buscar cliente
    3. Listar Cliente
    4. Salir """)
    op = input("Seleccione una opción ==> ")
    if op == "1":
        nombre = input("Ingrese un nombre ==> ")
        apellido = input("Ingrese un apellido ==> ")
        edad = int(input("Ingrese la edad ==> "))
        cli= [nombre,apellido,edad]
        clientes.append(cli)
        print("Cliente agregado al sistema")
        print(clientes)

    elif op == "2":
        encontrado = False
        nombre= input("ingrese el nombre que quiere buscar ==>")
        for cli in clientes:
            if cli[0]==nombre.lower():
                print(f"""
            NOMBRE : {cli[0]} {cli[1]}
            EDAD : {cli[2]}
                    """)
                encontrado = True
                break
        if encontrado == False:
            print("Cliente no encontrado...")
    
    elif op == "3":
        for cli in clientes:
            print(f"""
                NOMBRE : {cli[0]} {cli[1]}  
                EDAD : {cli[2]}
                    """)
    
    elif op == "0":
        break
    input("Presione cualquier tecla para terminar...")
