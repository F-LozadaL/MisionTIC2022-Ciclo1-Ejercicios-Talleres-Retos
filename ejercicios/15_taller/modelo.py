import json

__ordenes=[]
__menu=[]


def load_file():
    with open('menu.json') as menu:
        __menu=json.load(menu)
    with open('ordenes.json') as ordenes:
        __ordenes=json.load(ordenes)
        
def create():
    pass