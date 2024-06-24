



import random

productos=[]




def agregar_productos():
    cosas=input("Ingrese el nombre del producto")
    productos.append(cosas)






def ver_productos():
    print(productos,end="")





def modificar_productos():
    producto=input("Que producto desea modificar")
    if producto not in producto:
        print("Producto no encontrado")
    if producto in productos:
        print()






def eliminar_productos():
    producto=input("Que producto desea eliminar")
    if producto not in producto:
        print("Producto no encontrado")
    if producto in productos:
        print()





def guardar_archivos():
    print()
