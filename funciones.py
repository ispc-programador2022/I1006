import pandas as pd
import csv
import sqlite3
import cv2
import matplotlib.pyplot as plt

class Acciones:
    '''Aca almaceno las acciones de convertir los datos a csv,
    crear el data frame
    ''' 
    
    @staticmethod
    def auto_cvs(a,b,x):
        filename = x +".csv"
        with open("./base_datos/"+filename, "w") as csv_file:
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
            
 
    @staticmethod
    def show_base():
        '''Muestra Todos Los eventos Cargados en La Base
        '''
        m_con = sqlite3.connect('base_datos\Eventos_base.db')
        m_cursor = m_con.cursor()

        m_cursor.execute("SELECT * FROM Eventos")
        cols = m_cursor.fetchall()

        for col in cols:
            print(col)

        m_con.commit()
        m_con.close()
        
        
    @staticmethod
    def show_grafico():
        '''Mostrar imagen del Grafico Creada
        '''
        img = cv2.imread('base_datos\grafico_scrap2.png')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        plt.xticks([]), plt.yticks([])
        plt.imshow(img, cmap='viridis', interpolation=None)
        plt.show()