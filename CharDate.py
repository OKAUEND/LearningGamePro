
class CharDate(object):
    def __init__(self,name,HP,ATK):
        self.name = name
        self.HP = HP
        self.ATK = ATK

    def Attack(self,Partner):
        Partner.HP = Partner.HP - 200


    def Defence(self):
        pass


    def Heal(self):
        pass


