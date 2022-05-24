from bibiloteca import validar_nota 

def eje1():
    num = int(input("Ingrese un numero>>_"))
    while num >= 0:
        print(num, end='')
        if num != 0:
            print(',', end='')
        num -= 1

# eje1()


def eje2(num: int):
    for i in range(num):
        print("*"*(i+1))

# eje2(3)


def eje3(num: int):

    for i in range(1, num*2+1, 2):
        pir = i
        while (pir != -1):
            print(pir, end=' ')
            pir -= 2
        print()

# eje3(6)


def eje4():
    echo = ''
    while(echo != 'salir'):

        echo = input("?")
        print('echo>'+echo)

# eje4()


def eje5(dicc: str, frase: str):
    palabras = dicc.split(',')
    diccionario = {}
    for traduccion in palabras:
        espanol, ingles = traduccion.split(':')
        diccionario[espanol] = ingles

    frase_split = frase.split()
    frase_traducida = ''

    for palabra in frase_split:
        if palabra in diccionario.keys():
            frase_traducida += diccionario[palabra]+' '
        else:
            frase_traducida += palabra+' '

    return frase_traducida.strip()


# print(eje5("hola:hello,mundo:world,el:the,manzana:apple", "hola el mundo manzana lelo"))


def eje6():
    carro = {}
    articulo = ''
    total = 0
    while True:
        articulo = input('Articulo  (0 to exit)>>')
        if articulo == '0':
            break
        precio = int(input('Precio>>'))
        total += precio
        carro[articulo] = precio

    print("Lista de la compra")
    print('----------------------------------------------------------------')
    for i in carro:
        print(f'{i}\t\t ${carro[i]}')
    print('----------------------------------------------------------------')
    print(f'total\t\t ${total}')

# print(eje6())


def eje7():
    asignaturas = []
    asignatura = ''
    while True:
        asignatura = input('Ingrese asignatura>>')
        if asignatura == '0':
            break
        asignaturas += [asignatura]
    print('Yo estudio ', end='')
    for i in range(len(asignaturas)):
        print(asignaturas[i], end='')
        if i != len(asignaturas)-1:
            print(', ', end='')


# eje7()


def eje8():
    asignaturas = []
    asignatura = ''
    perdidas=[]
    
    while True:
        asignatura = input('Ingrese asignatura>>')
        if asignatura == '0':
            break
        asignaturas += [asignatura]

    for i in asignaturas:
        nota = float(input(f'Nota de {i}>>'))
        if nota>=0 and nota <=5:
            if nota <3:
                perdidas+=[i]
                
        else:
            print('Error: Rango de notas')
            continue 
    
    for i in perdidas:
        asignaturas.remove(i)    
    
    
    print('asignaturas a recuperar:')
    for i in perdidas:
        print(f' -{i}')

# eje8()

def eje9():
    palabra=input("Ingrese palabra>>")
    for i in range(len(palabra)//2+1):
        if palabra[i]==palabra[-i-1]:
            continue
        else:
            print('NO es palindromo')
            return
    
    print('ES palindromo')
    
    

# eje9()

def eje10(precios:str):
    precios_str=precios.split(',')
    
    precios_int=[]
    for i in precios_str:
        precios_int+=[int(i)]
    
    precios_int.sort()
    print(precios_int)

# eje10('50, 75, 46, 22, 80, 65, 8')
# print(dir(list))

def eje11():
    palabra=input("Ingrese palabra>>")
    vocals='aeiou'
    for v in vocals:
        print(f"{v}: {palabra.count(v)}") 
        
# eje11()

def eje12(texto:str):
    palabras=texto.split()
    dicc={}
    for pal in palabras:
        if pal not in dicc.keys():
            dicc[pal]=palabras.count(pal)
    return dicc


def eje12_2(dicc:dict):
    palabra=''
    fre=0
    for pal in dicc:
        if dicc[pal]>fre:
            palabra=pal
            fre=dicc[pal]
    return tuple([palabra,fre])        
    
print(eje12_2(eje12("man man man man fre fre o o o o o o o li li")))