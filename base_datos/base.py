import sqlite3
import csv




with open('Cordoba_Eventos.csv',encoding='utf-8',newline='') as File: 
    next(File, None) 
    reader = csv.reader(File,delimiter=',')

#Crear Base 
    sql = sqlite3.connect('./base_datos/Eventos_base.db')
    con = sql.cursor()

#Creamos la tabla si no existe
    con.execute(
        "CREATE TABLE IF NOT EXISTS Eventos(ID INTEGER PRIMARY KEY AUTOINCREMENT, eventos text, fecha text)")



    lista=list(reader)
    del(lista[0])
    datos_csv= tuple(lista)
    
#Se Agregan los datos
    con.executemany("INSERT INTO Eventos ('eventos', 'fecha') VALUES (?,?)", datos_csv)
    

#Cerramos el archivo y la conexion a la bd
sql.commit()
sql.close()
    

