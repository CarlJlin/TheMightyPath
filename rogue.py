from character import Character

class Rogue(Character):
    def __init__(self, name, surname):
        super().__init__(name, surname, base_ad=20, base_hp=50, base_res=25, base_mana=10, base_mp=7, base_agi=15,
                         ad_growth=4, hp_growth=5, res_growth=2, mana_growth=3, mp_growth=1, agi_growth=2)

    def backstab(self, target):
        damage = self.base_ad * 2
        target.take_damage(damage)
        print(f"{self.name} {self.surname} used Backstab on {target.name} {target.surname} causing {damage} damage.")