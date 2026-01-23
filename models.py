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