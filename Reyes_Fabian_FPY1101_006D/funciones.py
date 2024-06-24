#Funciones iniciales hechas por Martin



import random
import csv
productos=[]




def agregar_productos(productos):
    cosas=input("Ingrese el nombre del producto: ")
    productos.append(cosas)
    





def ver_productos(productos):
    print(productos,end="")
print()





def modificar_productos(productos):
    producto=input("Que producto desea modificar: ")
    if producto not in producto:
        print("Producto no encontrado")
    if producto in productos:
        print()






def eliminar_productos(productos):
    producto=input("Que producto desea eliminar: ")
    if producto not in producto:
        print("Producto no encontrado")
    if producto in productos:
        ask=input("Estas seguro de eliminar este producto  Si/No")
        if ask=="Si":
            productos.remove(producto)
        elif ask=="No":
            print()
        else:
            print("Yapue escriba las cosas bien")




def guardar_archivos():
    with open('Reyes_Fabian_FPY1101_006D/usuarios.csv', 'r')as archivo_csv:
        lector_csv=csv.DictReader(archivo_csv)
        productos=list(lector_csv)
        for i in range(1, len(archivo_csv)):
            for j in range(len(archivo_csv)):
                print(archivo_csv)
        print('')