#Importing from other modules
from models import Character, Warrior, Mage

#Make two instances of the character class - name, hp, stength, intelligence
character_one = Warrior("Hero", 100, 10)
character_two = Mage("Evil Wizard", 40, 15)

#Print the starting state of the two characters
print(character_one)
print(character_two)

#Only run the loop while both Characters are alive
while character_one.is_alive() and character_two.is_alive():
            
    #Get "Hero" to attack "Goblin" unless low hp, then cast Heal
    if character_one.is_alive() and character_one.should_heal():
        character_one.heal()
    else:
        character_one.attack(character_two)
        
    if not character_two.is_alive():
        print(f"{character_two.name} has died!")
        break
    
    #Print the ending state of the two characters
    print(character_one)
    print(character_two)
    
    #Get "Goblin" to attack "Hero"
    character_two.attack(character_one)
    if not character_one.is_alive():
        print(f"{character_one.name} has died!")
        break
    
    #Print the ending state of the two characters
    print(character_one)
    print(character_two)
