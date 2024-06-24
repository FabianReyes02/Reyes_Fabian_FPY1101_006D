#Menú principal, Martin Rivas, Fabian Reyes
import funciones as funciones
import time
#While para el menu principal del programa
while True:
    try:
        eleccion=int(input("*** Bienvenido a la tienda RR ***\n\n1.-Agregar producto\n2.-Ver todos los productos\n3.-Modificar un producot\n4.-Eliminar un producto\n5.-Guardar una colección en un archivo\n6.-Salir del programa\n"))
    except:
        print("Ingrese una opción valida")    
    else:
        if eleccion==1:
            
        elif eleccion==2:

        elif eleccion==3:

        elif eleccion==4:
        
        elif eleccion==5:

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