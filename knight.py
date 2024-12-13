from character import Character

class Knight(Character):
    def __init__(self, name, surname):
        super().__init__(name, surname, base_ad=25, base_hp=60, base_res=30, base_mana=7, base_mp=5, base_agi=10,
                         ad_growth=5, hp_growth=6, res_growth=3, mana_growth=3, mp_growth=1, agi_growth=1)

    def shield_bash(self, target):
        damage = self.base_ad * 1.5
        target.take_damage(damage)
        print(f"{self.name} {self.surname} used Shield Bash on {target.name} {target.surname} causing {damage} damage.")