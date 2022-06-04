from functools import reduce


def eje1(frase:str):
    
    palabras=frase.split()
    longitudes= [len(x) for x in palabras if x!='el']
            
    return longitudes

# print(eje1("el rápido zorro marrón salta sobre el perro perezoso"))

def eje2(nums:list):
    
    positivos= [x for x in nums if x>0]
    
    return positivos

# print(eje2([34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]))


def eje3(frase:str):
    
    dig='0123456789'
    con=set()
    
    con={x for x in frase if x in dig}
    
    
    return con

# print(eje3("Hello 12345 World 5602")) 

def eje4_1():
    list1=[x**2 for x in range(10)]
    list2=[2**i for i in range(13)]   
    
    print(list1)
    print(list2)

# eje4_1()

def eje5():
    list1=[x**3 for x in range(11)]
    
    print(list1)
    

# eje5()

def eje6_1():
    my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
    map_result = list(map(lambda x: round(x**2,3), my_floats)) # Arreglar esta instrucción
    print(map_result)
    
# eje6_1()

def eje6_2():
    my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
    filter_result = list(filter(lambda name: len(name)<=7, my_names)) # Arreglar esta instrucción
    print(filter_result)
    
# eje6_2()

def eje6_3():
    my_numbers = [4, 6, 9, 23, 5]
    reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers) # Arreglar esta instrucción
    print(reduce_result)
    
# eje6_3()

def eje7(nums:str):
    # list_num=[int(x) for x in nums.split()]
    
    list_num = nums.split()
    list=[int(x) for x in list_num]
    