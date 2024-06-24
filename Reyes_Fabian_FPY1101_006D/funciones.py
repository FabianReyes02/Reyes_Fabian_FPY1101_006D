#Funciones iniciales hechas por Martin



import random

codigos=[]
import csv

productos=[]
precios=[]
cantidades=[]


def agregar_productos():#en esta def definimos agregar productos con la funcion del append a la lista "productos"
    codigo=input("Ingrese el codigo del producto: ")
    codigos.append(codigo)
    producto=input("El nombre del producto: ")
    productos.append(producto)
    cantidad=input("Las cantidades a agregar: ")
    cantidades.append(cantidad)
    precio=input("El precio neto del producto: ")
    precios.append(precio)
def ver_productos():#aca hacemos un print de todo lo que es la lista productos
    print(productos,end="")
print()
def modificar_productos():
    producto=input("Que producto desea modificar: ")
    if producto not in producto:
        print("Producto no encontrado")
    if producto in productos:
        print()
def eliminar_productos():
    producto=input("Que producto desea eliminar: ")
    if producto not in producto:
        print("Producto no encontrado")
    if producto in productos:
        ask=input("Estas seguro de eliminar este producto  Si/No: ")
        if ask=="Si":
            productos.remove(producto)
            print("Esta hecho.")
        elif ask=="No":
            print()
        else:
            print("Yapue escriba las cosas bien")
def guardar_archivos():
    print()
    with open('Reyes_Fabian_FPY1101_006D/usuarios.csv', 'r')as archivo_csv:
        lector_csv=csv.DictReader(archivo_csv)
        productos=list(lector_csv)
        for i in range(1, len(archivo_csv)):
            for j in range(len(archivo_csv)):
                print(archivo_csv)
        print('')
