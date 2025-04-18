
import persona as p


class Studente(p.Persona):
    
    def __init__(self,nome,eta,voti):
        super().__init__(nome,eta)
        
        self.voti=voti
        
    def calcola_media(self):
        if self.voti:
            media=sum(self.voti) / len(self.voti)
            return media 
    
            
    def presentazione(self):
        media = self.calcola_media()
        return f"Sono uno studente, mi chiamo {self.get_nome()}, ho {self.get_eta()} anni e la mia media è {media:.2f}."

    
class Professore(p.Persona):
    
    def __init__(self,nome,eta,materia):
        super().__init__(nome,eta)
        self.materia=materia
            
    def presentazione(self):
        return f"Sono uno professore, mi chiamo {self.get_nome()}, ho {self.get_eta()} anni e insegno la seguente materia: {self.materia}."

       

