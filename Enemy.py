from CharDate import CharDate

class Enemy(CharDate):
    """description of class"""
    def __init__(self,name,MaxHP,ATK) :
        super().__init__(name,MaxHP,ATK)
        self.HP = MaxHP

    def info(self):
        print(self.name + ': HP ' + str(self.HP) + ' / ' + str(self.MaxHP))
        


