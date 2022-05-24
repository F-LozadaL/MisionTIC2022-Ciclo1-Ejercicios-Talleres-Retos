def cliente(informacion:dict):
    
    boleta={
        "nombre":informacion["nombre"],
        "edad":informacion["edad"],
        "atraccion":str,
        "apto":True,
        "primer_ingreso":informacion["primer_ingreso"],
        "total_boleta": 0.0
    }
    
    if informacion["edad"]>=7 and informacion["edad"]<15:
        boleta["atraccion"]="Sillas voladoras"
        boleta["total_boleta"]=10000
        if boleta["primer_ingreso"]:
            boleta["total_boleta"]*=0.95
    elif informacion["edad"]>=15 and informacion["edad"]<=18:
        boleta["atraccion"]="Carros chocones"
        boleta["total_boleta"]=5000
        if boleta["primer_ingreso"]:
            boleta["total_boleta"]*=0.93
    elif informacion["edad"]>18:
        boleta["atraccion"]="X-Treme"
        boleta["total_boleta"]=20000
        if boleta["primer_ingreso"]:
            boleta["total_boleta"]*=0.95
    else:
        boleta["atraccion"]="N/A"
        boleta["total_boleta"]="N/A"
        boleta["apto"]=False
    return boleta

cliente1={
    "id_cliente":1,
    "nombre":"Johana Fernandez",
    "edad":20,
    "primer_ingreso":True,
}
cliente2={
    "id_cliente":2,
    "nombre":"Gloria Suarez",
    "edad":3,
    "primer_ingreso":True,
}
cliente3={
    "id_cliente":3,
    "nombre":"Tatiana Suarez",
    "edad":17,
    "primer_ingreso":False,
}
cliente4={
    "id_cliente":4,
    "nombre":"Tatiana Ruiz",
    "edad":8,
    "primer_ingreso":False,
}

print(cliente(cliente4))