import sys   
import menu
from scrapeo import Scrapeo
from scrapeo2 import Scrapeo2
from funciones import Acciones


class Main:
    def __init__(self):
        '''aca inicia la clase controladora'''       
    #app
    #debo llamar un menu que elija los opciones       
    #Cordoba_Eventos.csv  Contiene Los Datos de Dos CSV de los scrapeos   
    menu.Menu.cartel()
    
     
if __name__ == '__main__':
    
    select = True
    while select:
        menu.Menu.op_menu()
        op = input(" Seleccione : ")
    
        if op == "0":
            sys.exit()
        
        if op == "1":            
            menu.Menu.op_1()    
            excel = Acciones.concat_csv(Scrapeo.var_df, Scrapeo2.var_df2)
            print(excel)
            select = True
            
        if op == "2":            
            menu.Menu.op_2()
            select = True
            
        if op == "3":            
            menu.Menu.op_3()
            select = True
            
            
        