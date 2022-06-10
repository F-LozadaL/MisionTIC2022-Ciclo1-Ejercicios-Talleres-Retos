import pandas as pd

    
def listaPeliculas(rutaFileCsv: str)->str:
    
    if rutaFileCsv.split('.')[-1]=='csv?raw=true':
    
        try:  
            df=pd.read_csv(rutaFileCsv) 
            df1=df[['Country', 'Language','Gross Earnings']]
            
            df2=df1.pivot_table(index=['Country', 'Language'])
            return df2.head(10)
            
        except:
            return "Error al leer el archivo de datos."
            
    else:
        return "Extensión inválida."
    
rutaFileCsv='https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true'

print(listaPeliculas(rutaFileCsv))

    