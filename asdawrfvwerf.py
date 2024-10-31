numero=input("Ingrese Un Numero")
documento=open(f"Tabla-{numero}.txt")
print(documento.read())
documento.close()