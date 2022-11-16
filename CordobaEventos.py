from bs4 import BeautifulSoup
import requests
html_text = requests.get('https://www.eventbrite.com.ar/d/argentina--c%C3%B3rdoba/free--events/').text
soup = BeautifulSoup(html_text, 'lxml')
lista = soup.find_all('section', class_='search-base-screen__search-panel')
for  listas in lista:
    Evento = listas.find_all('h3', class_='eds-event-card-content__title eds-text-color--ui-800 eds-text-bl eds-text-weight--heavy')
    Fecha = listas.find_all('div', class_='eds-event-card-content__sub-title eds-text-color--primary-brand eds-l-pad-bot-1 eds-l-pad-top-2 eds-text-weight--heavy eds-text-bm')
    Locacion = listas.find_all('div', class_='card-text--truncated__one')
    Folow = listas.find_all('div', class_='eds-text-weight--heavy')
event_list= list()
for event in Evento:
    event_list.append(event.text)

fe_list= list()
for fe in Fecha:
    fe_list.append(fe.text)

loc_list= list()
for loc in Locacion:
    loc_list.append(loc.text)

fo_list= list()
for fo in Folow:
    fo_list.append(fo.text)
    
    for i in zip(event_list, fe_list, loc_list, fo_list):
        print(i)
