import requests
from bs4 import BeautifulSoup
from funciones import Acciones

class Scrapeo2:
    html_text = requests.get('https://cordoba.gob.ar/category/ciudad/entretiene/').text
    soup = BeautifulSoup(html_text, 'lxml')
    lista = soup.find_all('div', class_="site-content")

    for  listas in lista:   
        Evento = listas.find_all('h2', class_='blog-entry-title entry-title')
        Fecha = listas.find_all('li', class_='meta-date')
  
  
    # Creacion de Listas con los datos obtenidos
    evento_list = list()
    for e in Evento:        
        evento_list.append(e.text)

    fecha_list = list()
    for f in Fecha:
        fecha_list.append(f.text)

    
    # Creo el archivo csv y el dataframe      
    csv = "datos2"
    Acciones.auto_cvs(evento_list,fecha_list, csv)
    var_df2 = Acciones.auto_df("./datos/datos2.csv") 


     
    
 

  
    #resultado = fun_scrap3(evento_list,fecha_list)
