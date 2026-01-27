#Parent class for the characters
class Character:
    def __init__(self, name, hp, strength):
        self.name = name
        self._hp = hp
        self._max_hp = hp
        self.strength = strength
        self.weapon = None
    @property    
    def hp(self):
        return self._hp
    
    @hp.setter
    def hp(self, value):
        if value > self._max_hp:
            self._hp = self._max_hp
        elif value < 0:
            self._hp = 0
        else:
            self._hp = value
              
    def __str__(self):
        return f"{self.name} (HP: {self._hp})"
    #FIX THIS PART - CHECK TICKET
    def attack(self, target):
        target.take_damage(self.strength + self.Weapon.damage)
    #FIX THIS PART - CHECK TICKET    
    def is_alive(self):
        return self._hp > 0
    
    def take_damage(self, damage_amount):
        self.hp -= damage_amount
        print(
            f"{self.name} took {damage_amount} damage. "
            f"remaining HP: {self._hp}"
        )
        
    def equip(self, weapon):
        self.weapon = weapon
        print(f"{self.name} equipped {weapon.name}!")
    
#Child class for "Warriors"
class Warrior(Character):
    
    def heal(self):
        self.hp += 10
        print(f"{self.name} the warrior casts Heal! HP is now {self._hp}")
        
    def should_heal(self):
        return self._hp <= 30
        
class Mage(Character):
    
    def __init__(self, name, hp, intelligence):
        #Pass a "0" in the position of the strength here so we don't need
        #to pass in a strength value on the instantiation in the main
        super().__init__(name, hp, 0)
        self.intelligence = intelligence
        
    def attack(self, target):
        target.take_damage(self.intelligence)
        
class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
        
    def __str__(self):
        print(f"<{self.name} ({self.damage} damage)")
        