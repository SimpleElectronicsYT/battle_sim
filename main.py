#Importing from other modules
from models import Character


while True:
    #Make two instances of the character class - name, hp, stength
    character_one = Character("Hero", 100, 10)
    character_two = Character("Goblin", 30, 5)
    
    #Print the starting state of the two characters
    print(character_one)
    print(character_two)
    
    #Get "Hero" to attack "Goblin"
    character_one.attack(character_two)
    
    #Print the ending state of the two characters
    print(character_one)
    print(character_two)
    
    #Exit the loop, we're done here
    break