

def opcion_menu_principal():
    print("1 - Nuevo Pedido")
    print("2 - Listar Pedidos")
    print("3 - Cobrar Pedido")
    print("0 - Salir")
    
    opcion=None
    
    while opcion==None:
        opcion = leer_entero()
        if opcion not in range(0,4):
            opcion=None
            
    return opcion
        

def imprimir_mensaje(mensaje:str):
    print(mensaje)
    
def leer_entero(mensaje="Ingrese un valor:", opcional = False):
    valor=None
    if not opcional:
        while valor == None:
            try:
                valor= int(input(mensaje))
            except:
                imprimir_mensaje("Entrada inválida: Se debe ingresar una opción numérica.") 
    else:
        try:
            valor= int(input(mensaje))
        except:
            valor=None
            
    return valor