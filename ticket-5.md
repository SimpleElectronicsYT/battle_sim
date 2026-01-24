Ticket #5: The Mage & Method Overriding

Description: We are introducing a new class: The Mage. The Mage is physically weak (0 Strength) but mentally strong (Intelligence). We need to change how the attack method works specifically for the Mage, without breaking the Warrior or the base Character.

Requirements:

    Update models.py:

        Create a class Mage that inherits from Character.

        Override __init__:

            The Mage needs to accept name, hp, and intelligence.

            Critial Step: You must initialize the parent data (name, hp) properly. However, since Character expects strength, pass 0 for strength to the parent.

            Then, store intelligence in a new attribute: self.intelligence.

        Override attack:

            Define an attack method inside Mage (same name as the parent method).

            Logic: It should subtract self.intelligence from the target.hp.

            Print: "Mage casts Fireball on [target] for [intelligence] damage!"

    Update main.py:

        Change character_two from a "Goblin" Character to an "Evil Wizard" Mage.

            Give him 40 HP and 15 Intelligence.

        Important: Do not change the game loop code. The loop calls .attack(). It shouldn't care if the object is a Warrior or a Mage; it should just work.

Acceptance Criteria:

    The Hero heals when low.

    The Evil Wizard attacks using "Fireball" and deals 15 damage (his Intelligence), not 0 (his Strength).

    The console output clearly distinguishes between the Warrior's physical attacks and the Mage's magical attacks.

Conceptual Hint:

    When you write an __init__ in a child class, you overwrite the parent's setup. To keep the parent's setup logic (like setting name and hp), you need to call: super().__init__(name, hp, strength)