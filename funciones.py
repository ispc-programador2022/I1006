import pandas as pd
import csv


class Acciones:
    '''Aca almaceno las acciones de convertir los datos a csv,
    crear el data frame
    ''' 
    
    @staticmethod
    def auto_cvs(a,b,x):
        filename = x +".csv"
        with open("./datos/"+filename, "w") as csv_file:
            csv_writer = csv.writer(csv_file, dialect='excel')
            csv_writer.writerows(zip(a, b))
        return
    
    
    @staticmethod
    def auto_df(x):
        
        '''Selecciono el csv y uso el encoding para leer el excel
        Uso header None para colocar una cabecera vacia
        Con columns creo los Nombres de las Columnas
        '''
        datos_df = pd.read_csv(x,encoding='latin1',  header=None )
        datos_df.columns = ["Evento","Fecha"]
       
        return datos_df
    
    
