#Parent class for the characters
class Character:
    def __init__(self, name, hp, strength):
        self.name = name
        self._hp = hp
        self.strength = strength
        
    def __str__(self):
        return f"{self.name} (HP: {self._hp})"
    
    def attack(self, target):
        target.take_damage(self.strength)
        
    def is_alive(self):
        return self._hp > 0
    
    def take_damage(self, damage_amount):
        self._hp -= damage_amount
        if self._hp < 0:
            self._hp = 0
        print(
            f"{self.name} took {damage_amount} damage. "
            f"remaining HP: {self._hp}"
        )
    
#Child class for "Warriors"
class Warrior(Character):
    
    def heal(self):
        self._hp += 10
        print(f"{self.name} the warrior casts Heal! HP is now {self._hp}")
        
    def should_heal(self):
        return self._hp <= 30
        
class Mage(Character):
    
    def __init__(self, name, hp, intelligence):
        #Pass a "0" in the position of the strength here so we don't need
        #to pass in a strength value on the instanciation in the main
        super().__init__(name, hp, 0)
        self.intelligence = intelligence
        
    def attack(self, target):
        target.take_damage(self.intelligence)
        