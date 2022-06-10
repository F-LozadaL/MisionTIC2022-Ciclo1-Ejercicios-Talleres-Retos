def AutoPartes(ventas:list):
    dicc={}
    for ve in ventas:
        
        if str(ve[0]) in dicc :
            dicc[str(ve[0])]+=[ve]
        else:
            dicc[str(ve[0])]=[ve]
            
        
    
    return dicc

def consultaRegistro(ventas, idProducto):
    reg = ventas
    if str(idProducto) in reg.keys(): 
        con=reg[str(idProducto)]
        for ve in con:
            msg=(f"Producto consultado : {ve[0]}  Descripción  {ve[1]}  #Parte  {ve[2]}  Cantidad vendida  {ve[3]}  Stock  {ve[4]}  Comprador {ve[5]}  Documento  {ve[6]}  Fecha Venta  {ve[7]}")
            print (msg)
    else:
        print("No hay registro de venta de ese producto")
    
            
        



# consultaRegistro(AutoPartes([(2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
#     (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
#     (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
#     (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
#     (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]), 2010)

# consultaRegistro(AutoPartes([
#     (5489,'tornillo', 'RS8512',2,33,'Julio Perez',3654213,'13/06/2020'),
#     (3215,'zocalo', 'UM8587',2,125,'Laura Macias',1256321,'13/06/2020'),
#     (3698,'biela', 'PT3218',1,78,'Luis Peña',14565487,'13/06/2020'),
#     (8795,'cilindro', 'AZ8794',2,96,'Carlos Casio',5612405,'13/06/2020')]), 2001)

consultaRegistro(AutoPartes([
    (2564,'Cárter', 'PT29872',2,32,'Peter Cerezo',8545436,'16/06/2020'),
    (5412,'válvula', 'AZ8798',2,11,'Juan Peña',568975,'16/06/2020')]), 5412)