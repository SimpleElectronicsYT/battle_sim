Ticket #2: Basic Combat Interaction

Description: A character that just sits there with 100 HP isn't very fun. We need them to interact. We are going to implement the ability for one character to damage another.

Requirements:

    Update Character class (models.py):

        Add a method called attack.

        This method should take self and one other argument: target (this will be the Character object being attacked).

        The Logic:

            Subtract the attacker's strength from the target's hp.

            Print a message to the console explaining what happened (e.g., "Hero attacks Goblin for 10 damage!").

    Update Game Loop (main.py):

        Create two instances of Character:

            hero (Name: "Hero", HP: 100, Strength: 10)

            enemy (Name: "Goblin", HP: 30, Strength: 5)

        Call the attack method: Have the hero attack the enemy.

        Print the enemy object afterward to verify their HP has actually gone down.

Acceptance Criteria:

    Running main.py shows the attack message and the Goblin's HP dropping from 30 to 20.

Hint:

    Remember, because target is an object (an instance of the Character class), you can access and modify its attributes (like target.hp) directly inside the attack method using dot notation.