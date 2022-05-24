def eje6():
   
    deposito=0
    orden='0'

    while(True):
        
        orden = input(" Accion (Linea Vacia para Salir)>>").split()
        if len(orden)==2:
            accion,cantidad = orden
        else:
            if orden==[]:
                print('Deposito',deposito)
                print("Salida Exitosa")
                return
            print("Error: orden mal formulada")
            continue
        cantidad=int(cantidad)
        
        if(accion not in "DdRr"):
            print("Error: opcion no aceptada")
            continue
        
        if accion =='d' or accion == 'D':
            deposito += cantidad
        elif accion == 'r' or accion == 'R':
            deposito -= cantidad
            

        
    
    
    
print(eje6())