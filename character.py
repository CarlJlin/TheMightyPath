class Character:
    def __init__(self, name, surname, base_ad, base_hp, base_res, base_mana, base_mp, base_agi, ad_growth, hp_growth, res_growth, mana_growth, mp_growth, agi_growth):
        self.name = name
        self.surname = surname
        self.level = 1
        self.exp = 0
        self.to_level_up = 100
        self.exp_ratio = 0

        self.base_ad = base_ad
        self.base_hp = base_hp
        self.base_res = base_res
        self.base_mana = base_mana
        self.base_mp = base_mp
        self.base_agi = base_agi

        self.ad_growth = ad_growth
        self.hp_growth = hp_growth
        self.res_growth = res_growth
        self.mana_growth = mana_growth
        self.mp_growth = mp_growth
        self.agi_growth = agi_growth

    def levelup(self):
        self.level += 1
        self.to_level_up *= self.exp_ratio

        self.base_ad += self.ad_growth
        self.base_hp += self.hp_growth
        self.base_res += self.res_growth
        self.base_mana += self.mana_growth
        self.base_mp += self.mp_growth
        self.base_agi += self.agi_growth

    def gainEXP(self, exp):
        self.exp += exp
        if self.exp >= self.to_level_up:
            self.exp -= self.to_level_up
            self.levelup()

    def __str__(self):
        return (f"{self.__class__.__name__} {self.name} {self.surname}: Level {self.level}, EXP {self.exp}, AD {self.base_ad}, "
                f"Mana {self.base_mana}, MP {self.base_mp}, Agility {self.base_agi}")