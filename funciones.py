import pandas as pd
import csv
import sqlite3

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
  
  
    @staticmethod
    def concat_csv(a,b):
        '''Concatenar Los Datos de los Eventos
        '''
        cvs_1 = a
        cvs_2 = b      
        final_dataframe = pd.concat([cvs_1, cvs_2]).drop_duplicates( 
            subset='Evento', keep='last').reset_index(drop=True)    
        final_dataframe.to_csv('Cordoba_Eventos.csv', index=False)        
        print(final_dataframe)
        return 
            
 
        