numero=int(input("Ingrese El Numero De La Tabla"))
archivo=open("Tabla-"+str(numero)+".txt","w")
archivo.write(f"Tabla de multiplicar del {numero}:"\n") 
for i in range(1, 11):
    archivo.write(str(numero)+ "X"+ str(i) +"="+ str(numero * i)+"\n" )

archivo.close()