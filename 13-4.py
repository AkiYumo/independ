class Horse:

    def __init__(self,owner):
        self.owner= owner
        print("Created")
        
class Rider:
    
    def __init__(self,name,H):
        self.name = name
        self.H = H
        print("created")

kouhei = Rider("kouhei",161)
deep = Horse(kouhei)
