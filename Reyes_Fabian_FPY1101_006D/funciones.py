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
    with open('usuarios.csv', 'w')as usuarios:
        for i in range(1, len(usuarios)):
            for j in range(len(usuarios)):
            