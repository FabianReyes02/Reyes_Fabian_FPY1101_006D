#Menú principal, Martin Rivas, Fabian Reyes
import funciones as f
import time
#While para el menu principal del programa
while True:
    try:
        eleccion=int(input("*** Bienvenido a la tienda RR ***\n\n1.-Agregar producto\n2.-Ver todos los productos\n3.-Modificar un producot\n4.-Eliminar un producto\n5.-Guardar una colección en un archivo\n6.-Salir del programa\n:"))
    except:
        print("Ingrese una opción valida")    
    else:
        if eleccion==1:
            print("Usted va a agregar un producto nuevo.\n")
            f.agregar_productos()
        elif eleccion==2:
            print("Usted va a ver todos los productos.\n")
            f.ver_productos()
        elif eleccion==3:
            print("Usted va a modificar un procuto.\n")
            f.ver_productos()
        elif eleccion==4:
            f.eliminar_productos()
            print("Usted va a eliminar un producto.\n")
        elif eleccion==5:
            print("Usted va a guardar una colección.\n")
            f.guardar_archivos()
        elif eleccion==6:
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("Gracias por visitar la tienda RR")
            break
        else:
            print("Ingrese una opción valida")