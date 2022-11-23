from bs4 import BeautifulSoup
import requests
import pandas as pd
from funciones import Acciones

class Scrapeo:
    
    html_text = requests.get('https://www.eventbrite.com.ar/d/argentina--c%C3%B3rdoba/free--events/').text
    soup = BeautifulSoup(html_text, 'lxml')
    lista = soup.find_all('section', class_='search-base-screen__search-panel')
    
    
    for  listas in lista:
        Evento = listas.find_all('h3', class_='eds-event-card-content__title eds-text-color--ui-800 eds-text-bl eds-text-weight--heavy')
        Fecha = listas.find_all('div', class_='eds-event-card-content__sub-title eds-text-color--primary-brand eds-l-pad-bot-1 eds-l-pad-top-2 eds-text-weight--heavy eds-text-bm')
        #Locacion = listas.find_all('div', class_='card-text--truncated__one')
        #Folow = listas.find_all('div', class_='eds-text-weight--heavy')
       
        
    event_list= list()
    for event in Evento:
        event_list.append(event.text)

    fe_list= list()
    for fe in Fecha:
        fe_list.append(fe.text)


    csv = "datos"
    Acciones.auto_cvs(event_list,fe_list, csv)
    data = Acciones.auto_df("./base_datos/datos.csv") 
    
    #Con esto borro filas duplicadas
    var_df = data.drop_duplicates(subset=['Evento'])
 