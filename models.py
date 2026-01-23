class Character:
    def __init__(self, name, hp, strength):
        self.name = name
        self.hp = hp
        self.strength = strength
        
    def __str__(self):
        return f"{self.name} (HP: {self.hp})"
        
