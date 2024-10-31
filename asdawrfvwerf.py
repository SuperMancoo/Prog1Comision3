print("Ejercicio de prueba.")
numero=input("Ingrese Un Numero:" )
documento=open(f"Prog1Comision3\\Tabla-{numero}.txt")

lineas = documento.readlines()
for linea in lineas:
    print(linea)

documento.close()