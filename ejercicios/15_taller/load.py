
import json


menu={
    "Sopa":{'Sancocho':3000, 'Ajiaco':2500},
    "Principio":{'Alberjas':1500,'lentejas':1200},
    "Carne":{'Pollo':3000, 'Carne':3500},
    "Ensalada":1000,
    "Jugo":['Mango','Maracuya','Mora',500]
}

def cargar_menu(menu:list):
    with open('ejercicios/15_taller/menu.json','w') as archivo_menu:
        json.dump(menu,archivo_menu, indent=4)




cargar_menu(menu)