def CDT (usuario : str, capital : int, tiempo : int):
      '''CDT
            :Parámetros:      usuario (str): alfanumérico
      que identifica el usuario capital (int): 
      Monto a ingresar     tiempo (int): Tiempo del 
      CDT
      :
            String: de la forma "las ganancias obtenidas por un monto de {}, en un tiempo {} es: 
      {}" para el caso de las ganacias, para las "La cantidad de dinero a recibir, segun el monto inicial
      {}, para un tiempo de {} es: {}"
      '''
      valor_total=0
      if(tiempo>2):
            valor_total=capital+(capital*0.03*tiempo)/12
      else:
            valor_total=capital*(1-0.02)
      respuesta=f"Para el usuario {usuario}, La cantidad de dinero a recibir, según el monto inicial {capital}, para un tiempo de {tiempo}, meses es:,{int(valor_total)}"
      return respuesta


# usuario1="AB1012"
# monto_inicial1=1000000
# meses1=3
# valor_total1=monto_inicial1+(monto_inicial1*0.03*meses1)/12

# print(CDT(usuario1,monto_inicial1,meses1))

# usuario2="ER3366"
# monto_inicial2=650000
# meses2=2
# valor_total2=monto_inicial2 - monto_inicial2*0.02

# print(type(CDT(usuario2,monto_inicial2,meses2)))
