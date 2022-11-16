from scrapeo3 import Scrapeo

class Menu:
    
    def op_menu():
        print("\n")
        print("                  A G E N D A                 ")
        print(" --------------------------------------------")
        print(" |     All Eventos Cordoba:              1  |")
        print(" |     Ver Cordoba Free Eventos:         2  |")
        print(" |     Ver Cordoba Capital Eventos:      3  |")
        print(" |     Ver Eventos Ciudad Entretiene:    4  |")       
        print(" |                  EXIT:                0  |")
        print("\n")
        
    def op_1():       
        print("\n","  ==== Eventos Cordoba ====  ","\n")    
        print("\n")
        
        return
    def op_2():       
        print("\n","  ==== SCRAP 1 ====  ","\n")    
        print("\n")
        return
    
    def op_3():       
        print("\n","  ==== SCRAP 2 ====  ","\n")    
        print("\n")
        return
    
    
    def op_4():       
        print("\n","  ==== SCRAP 3 ====  ","\n")    
        print(Scrapeo.var_df)
        return

