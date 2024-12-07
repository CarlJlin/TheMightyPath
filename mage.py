from character import Character

class Mage(Character):
    def __init__(self, name, surname):
        super().__init__(name, surname, base_ad=15, base_hp=35, base_res=12, base_mana=50, base_mp=40, base_agi=5,
                         ad_growth=1.5, hp_growth=3.5, res_growth=1.5, mana_growth=6, mp_growth=5, agi_growth=1.5)