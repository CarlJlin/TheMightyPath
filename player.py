from knight import Knight
from mage import Mage
from rogue import Rogue
from enum import Enum

class DifficultyLevel(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3

class Player:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.character = None
        self.difficulty = None
        self.exp_ratio = 1.0
        self.res_ratio = 1.0
        self.friends = []

    def choose_class(self):
        while True:
            class_choice = input("Choose your class (Knight, Mage, Rogue): ").strip().lower()
            if class_choice == 'knight':
                self.character = Knight(self.name, self.surname)
                break
            elif class_choice == 'mage':
                self.character = Mage(self.name, self.surname)
                break
            elif class_choice == 'rogue':
                self.character = Rogue(self.name, self.surname)
                break
            else:
                print("Wrong naming. Choose exactly between 'Knight', 'Mage', and 'Rogue'.")

    def choose_difficulty(self):
        while True:
            try:
                difficulty = int(input("Difficulty: (1, 2, 3) "))
                if difficulty in DifficultyLevel._value2member_map_:
                    self.difficulty = DifficultyLevel(difficulty)
                    self.exp_ratio = {DifficultyLevel.EASY: 2.2, DifficultyLevel.MEDIUM: 2.7, DifficultyLevel.HARD: 3.2}[self.difficulty]
                    self.res_ratio = {DifficultyLevel.EASY: 2, DifficultyLevel.MEDIUM: 2.5, DifficultyLevel.HARD: 3}[self.difficulty]
                    self.character.exp_ratio = self.exp_ratio
                    break
                else:
                    print("Wrong difficulty. Choose only between 1, 2, or 3.")
            except ValueError:
                print("Invalid input. Please enter a number (1, 2, or 3).")

    def gainEXP(self, exp):
        self.character.gainEXP(exp)

    def take_damage(self, damage):
        actual_damage = max(0, damage - (self.character.base_res / self.res_ratio))
        self.character.base_hp -= actual_damage
        print(f"{self.character.name} {self.character.surname} took {actual_damage} damage and has {self.character.base_hp} health left.")

    def add_friend(self, friend_name, friend_surname, friend_class):
        if friend_class == 'knight':
            friend = Knight(friend_name, friend_surname)
        elif friend_class == 'mage':
            friend = Mage(friend_name, friend_surname)
        elif friend_class == 'rogue':
            friend = Rogue(friend_name, friend_surname)
        else:
            print("Invalid class for friend.")
            return
        self.friends.append(friend)

    def use_ability(self, ability_name, target):
        if hasattr(self.character, ability_name):
            ability = getattr(self.character, ability_name)
            ability(target)
        else:
            print(f"{self.character.name} {self.character.surname} does not have the ability {ability_name}.")

    def __str__(self):
        friends_str = ''.join(str(friend) for friend in self.friends)
        return f"{self.character}\nFriends:\n{friends_str}"