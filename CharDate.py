
class CharDate(object):
    def __init__(self,name,MaxHP,ATK):
        self.name = name
        self.MaxHP = MaxHP
        self.ATK = ATK
        self.Guard = 0

    def Attack(self,EnemyDate):
        LocalATK = self.ATK
        if EnemyDate.Guard > 0:
            LocalATK /= EnemyDate.Guard
            
        EnemyDate.HP = EnemyDate.HP - LocalATK 


    def Defence(self):
        self.Guard = 2
    

    def Heal(self):
        HealHP = self.HP + 200
        if HealHP > self.MaxHP:
            self.HP = self.MaxHP
        else:
            self.HP = HealHP
