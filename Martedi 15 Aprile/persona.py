
class Persona():
    def __init__(self,nome,eta):
    #inizializzare nome e età   
        self.__nome=nome 
        self.__eta=eta
        
    def presentazione(self):
        print(f"{self.__nome} ha {self.__eta} anni")
        
    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome 
        
    def get_eta(self):
        return self.__eta

    def set_eta(self, eta):
        self.__eta = eta
        


    
        