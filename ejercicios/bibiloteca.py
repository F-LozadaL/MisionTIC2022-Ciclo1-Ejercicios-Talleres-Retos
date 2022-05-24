def validar_nota(planilla=''):
    nota = float(input(planilla))
    if nota>=0 and nota <=5:
        if nota >=3:
            return True
        else:
            return False
    print('Error: Rango de nota ingresado !0-5')
    return 