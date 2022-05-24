

def eje1(num:int):
    if (num%2==0) and ((num//2)%2==0):
        return True
    else:
        return False

def eje2(horas:int,tarifa:float):
    if horas>40:
        return horas*tarifa + (horas-40)*tarifa*1.5
    else: 
        return horas*tarifa

# def eje3()

def eje4():
    nombre=input("introduzca su nombre: ")
    num= int(input("Introduzca un numero: "))
    nombre+= "\n"
    print(nombre * num)

def eje5():
    nombre=input("introduzca su nombre: ")
    
    print(f"{nombre} tiene {len(nombre)} letras")

def eje6():
    tel=input("introduzca su numero telefonico: ")
    lis=tel.split('-')
    print(lis[1])

def eje7(nota1:float,nota2:float,nota3:float):
    if(nota1<0 or nota1 >5):
        return "nota 1 no valida"
    if(nota2<0 or nota2 >5):
        return "nota 2 no valida"
    if(nota3<0 or nota3 >5):
        return "nota 3 no valida"

    promedio =(nota1+nota2+nota3)/3
    if promedio>=3:
        return f"Feliciataciones aprobaste con promedio de {round(promedio,2)}"
    else: 
        return f"Desaprobaste con promedio de {promedio}"
    
    
def eje8 (precio:float):
    if precio <0:
        return "precio no valido"
    elif precio <100000:
        return f"el descuento por este producto es de {0}"
    elif precio <225000:
        return f"el descuento por este producto es de {precio*0.015}"
    elif precio <375000:
        return f"el descuento por este producto es de {precio*0.038}"
    else:
        return f"el descuento por este producto es de {precio*0.015}"
    
    
def eje9(numa:float,numb:float, numc:float):
    
    if numa ==0 :
        return "no hay solucion"
    if ((numb**2 - 4*numc*numa)<0):
        return f"no hay solucion: {numb**2 - 4*numc*numa}"
    else:
        sol1=((numb**2 - 4*numc*numa)**(1/2)-numb)/2*numa
        sol1=round(sol1,2)
        sol2=((numb**2 - 4*numc*numa)**(1/2)+numb)/2*numa
        sol2=round(sol2,2)
        if(sol1==sol2):
            return f"Sol hay una solucion y es {sol1}"
        else:    
            return f"las soluciones son {sol1} y {sol2}"



print (eje9(4,6,1))