#Funciones iniciales hechas por Martin



import random

codigos=[]
import csv

productos=[]
precios=[]
cantidades=[]


def agregar_productos():#en esta def definimos agregar productos con la funcion del append a la lista "productos"
        print("Usted va a agregar un producto nuevo.\n")
        codigo=input("Ingrese el codigo del producto: ")
        codigos.append(codigo)
        producto=input("El nombre del producto: ")
        productos.append(producto)
        cantidad=input("Las cantidades a agregar: ")
        cantidades.append(cantidad)
        precio=input("El precio neto del producto: ")
        precios.append(precio)
def ver_productos():#aca hacemos un print de todo lo que es la lista productos
    print("Usted va a ver todos los productos.\n")
    print(codigos,end="")
    print()
    print(productos,end="")
    print()
    print(precios,end="")
    print()
    print(cantidades,end="")
    print()
def modificar_productos():
    print("Usted va a modificar un producto.\n")
    producto=input("Que producto desea modificar: ")
    if producto not in producto():
        print("Producto no encontrado")
    if producto in productos:
        print()
def eliminar_productos():
    print("Usted va a eliminar un producto.\n")
    producto=input("Que producto desea eliminar: ")
    if producto not in producto:
        print("Producto no encontrado")
    while True:
        if producto in productos:
            ask=input("Estas seguro de eliminar este producto  Si/No: ")
            if ask=="Si":
                productos.remove(producto)
                print("Esta hecho.")
                break
            elif ask=="No":
                print()
                break
            else:
                print("Yapue escriba las cosas bien")
def guardar_archivos():
    archivo=open('Reyes_Fabian_FPY1101_006D/Reyes_Fabian_FPY1101_006D/usuarios.csv', 'a')
    archivo.write(f"{codigos},{productos},{cantidades},{precios}\n")
