from socket import MsgFlag
from sqlite3 import InterfaceError


def eje1 (nota:float):
    msg=""
    if nota>0 and nota <5:
        if nota > 4.0:
            msg="Felicitaciones"
        return f"Su nota es {nota} {msg}"
    else:
       return f"nota no valida"
   
def eje2(nota:float):
    
    if nota>0 and nota <5:
        if(nota>=3.0):
            print(f"Su nota es: {nota}, Ganó el curso")
        else:
            print(f"Su nota es: {nota}, Perdió el curso")
    else:
        print("nota no valida")

def eje3():
    msg=""
    nombre=input("Ingrese su Nombre_")
    age=int(input("Ingrese su edad_"))
    if(age>=18):
        msg=f"{nombre} es mayor de edad"
    else:
        msg=f"{nombre} es menor de edad"
    return msg

def eje4(num:int):
    msg=""
    if num % 2 == 0:
        msg=f"el numero {num} es par"
    else:
        msg=f"el numero {num} es impar"
    return msg

def eje5 (num:float):
    
    if(num>3.8 & num <=7.8):
        return True
    else:
        return False
    
def eje6 (num:float):
    
    if(num>3.8 & num <=7.8):
        return True
    if(num>4.5 & num <=9.3):
        return True
    if(num>=23.4 & num <=45.3):
        return True
    return False

def eje7 ():
    char=input("Ingrese OS_")
    if(char=='a'):
        print("Android")
    elif(char=="i"):
        print ("IOS")
    else:
        print ("Opcion inválida")
        

def eje8(nota:float):
    
    
    if nota>0 and nota <5:
        if(nota<3.0):
            print("Insuficiente")
        elif nota <=3.5:
            print("Aceptable")
        elif nota <=4.0:
            print("Sobresaliente")
        elif nota ==5:
            print("Excelente")
    else:
        print("nota no valida")
        
def eje9 (num1:int,num2:int,num3:int,num4:int):
    if num1 > num2:
        if num1 > num3:
            if num1 > num4:
                return num1
            else:
                return num4
        else:
            if num3 > num4 :
                return num3
            else:
                return num4
    else:
        if num2 > num3:
            if num2 > num4:
                return num2
            else:
                return num4
        else:
            if num3 > num4:
                return num3
            else:
                return num4

def eje10(estrato:int,metros:float):
    total=0
    msg=''
    er=False
    
    print(estrato>6)
    
    if estrato<1 or estrato>6:
        msg = 'Estrato no valido'
        er=True
    if metros<0:
        if(er):
            msg+=" | "
            
        msg+="Valor de metros cubicos consumidos no valido"
        er=True
        
    if er:
        return msg
    
    if estrato == 1:
        total += (8000 + metros*2200)
    elif estrato==2:
        total += (9000 + metros*2350)
    elif estrato==3:
        total += (10400 + metros*2600)
    elif estrato==4:
        total += (11900 + metros*3400)
    elif estrato==5:
        total += (13400 + metros*3900)
    else:
        total += (15400 + metros*4800)

    return f"El valor total de la factura a pagar es de: {total}"
        
def eje11 (genero:str, altura:float, edad:int, pareja:bool):
    er=False
    msg=''
    if genero =='M' or genero =='m':
        if altura<1.65 :
            msg = "Altura menor a 1.65"
            er = True
            
        if edad<18 or edad>24:
            if er:
                msg += " | "
            msg += " Edad fuera del rango"
            er = True
        
        if pareja:
            if er:
                msg += " | "
            msg += "No es soltero"
            er = True
        if er:
            msg= "No es apto: " + msg
            
        if not er:
            msg="Apto para prestar servicio militar" 
            
    elif genero =='F' or genero =='f':
        
        if altura<1.60:
            msg = "Altura menor a 1.60"
            er = True

            
        if edad<20 or edad>25:
            if er:
                msg+=" | "
            msg += " Edad fuera del rango"
            er = True
        
        if pareja:
            if er:
                msg += " | "
            msg+="No es soltera"
            er = True
        
        if er:
            msg= "No es apta: " + msg
        
        if not er:
            msg= "Apta para prestar servicio militar" 
            
    else:
        print('Sexo no valido')
    

    
    return msg

amigo_1={
    "nombre":"Camilo",
    "capacidad_vaso":2.0,
    "capacidad_actual":1.0,
}
amigo_2={
    "nombre":"Andres",
    "capacidad_vaso":1.7,
    "capacidad_actual":1.0,
}
amigo_3={
    "nombre":"Juan",
    "capacidad_vaso":1.8,
    "capacidad_actual":1.0,
}

def desperdicio_de_gaseosa(amigo_1:dict,amigo_2:dict, amigo_3:dict,capacidad_boton:float):
    faltante_1=amigo_1["capacidad_vaso"]-amigo_1["capacidad_actual"]
    faltante_2=amigo_2["capacidad_vaso"]-amigo_2["capacidad_actual"]
    faltante_3=amigo_3["capacidad_vaso"]-amigo_3["capacidad_actual"]
    exceso_1=False
    exceso_2=False
    exceso_3=False
    lista_exceso={}
    if capacidad_boton>faltante_1:
        exceso_1=True
        lista_exceso.insert(0,faltante_1)
    if capacidad_boton>faltante_2:
        exceso_2=True
        lista_exceso.insert(1,faltante_2)
    if capacidad_boton>faltante_3:
        exceso_3=True
        lista_exceso.insert(2,faltante_3)
    
    lista_exceso.sort()
    
    
    if exceso_1==False and exceso_2== False and exceso_3== False:
        return None
    
    return