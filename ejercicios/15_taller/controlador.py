
import vista as vst
import modelo as mdl

def menu_principal():
    mdl.load_file()
    try: 
        mainloop = True
        while mainloop: 
            
            opcion = vst.opcion_menu_principal()

            if opcion == 1:
                nuevo_pedido()
            elif opcion == 2:
                print (__menu)
                pass
            elif opcion == 3:
                pass
            elif opcion == 0:
                mainloop = False
            else:
                pass
            
    except Exception as e:
        vst.mostrar_error(e)
        
def nuevo_pedido():
    
    pass