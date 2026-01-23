Ticket #3: The Battle Loop & Death

Description: A single punch isn't a fight. We need a loop that continues until someone runs out of HP. We also need a clean way to check if a character is dead without checking if hp <= 0 everywhere in our main file.

Requirements:

    Update Character class (models.py):

        Add a method called is_alive(self).

        It should return True if self.hp is greater than 0, and False otherwise.

    Update Game Loop (main.py):

        Initialization: Move the character creation outside the while loop.

        The Loop Condition: Change while True: to check your new method. We want to loop while the Hero is alive and the Goblin is alive.

        Turn Logic:

            Hero attacks Enemy.

            Check: If the Enemy died from that hit, print "Goblin has died!" and break the loop (or let the while condition handle it).

            (Only if Enemy is still alive) Enemy attacks Hero.

            Check: If Hero died, print "Hero has died!".

Acceptance Criteria:

    The script runs a fight to the death.

    It prints the attack messages turn by turn.

    It ends gracefully when one character reaches 0 or less HP.

Hint:

    while hero.is_alive() and enemy.is_alive(): is a very readable way to start your loop!