#Parent class for the characters
class Character:
    def __init__(self, name, hp, strength):
        self.name = name
        self.hp = hp
        self.strength = strength
        
    def __str__(self):
        return f"{self.name} (HP: {self.hp})"
    
    def attack(self, target):
        target.hp -= self.strength
        print(f"{self.name} attacks {target.name} for {self.strength} damage!")
        
    def is_alive(self):
        return self.hp > 0
    
#Child class for "Warriors"
class Warrior(Character):
    
    def heal(self):
        self.hp += 10
        print(f"{self.name} the warrior casts Heal! HP is now {self.hp}")
        
class Mage(Character):
    
    def __init__(self, name, hp, intelligence):
        #Pass a "0" in the position of the strength here so we don't need
        #to pass in a strength value on the instanciation in the main
        super().__init__(name, hp, 0)
        self.intelligence = intelligence
        
    def attack(self, target):
        target.hp -= self.intelligence
        print(f"{self.name} casts Fireball on {target.name} for {self.intelligence} damage!")
        