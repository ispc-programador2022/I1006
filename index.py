import sys   
import menu




class Main:
    def __init__(self):
        '''aca inicia la clase controladora'''
        
    # lanzo desde aca la app
    #debo llamar un menu que elija los opciones
        
        
if __name__ == '__main__':
    
    select = True
    while select:
        menu.Menu.op_menu()
        op = input(" Seleccione : ")
    
        if op == "0":
            sys.exit()
        
        if op == "1":            
            menu.Menu.op_1()
            select = True
            
        if op == "2":            
            menu.Menu.op_2()
            select = True
            
        if op == "3":            
            menu.Menu.op_3()
            select = True
        #de momento solo esta funcion esta cargada    
        if op == "4":            
            menu.Menu.op_4()
            select = True
            
        