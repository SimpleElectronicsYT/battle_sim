Ticket #1: Project Setup & Base Character Model

Description: We need the foundation for our battle simulator. Before we can have anyone fighting, we need to define what a "Character" actually is and set up our workspace so we aren't writing everything in a single script.

Requirements:

    Folder Structure:

        Create a root directory for the project (e.g., battle_sim).

        Inside that, create two empty Python files:

            models.py (This will hold our class definitions).

            main.py (This will eventually run the game loop).

    The Character Class (models.py):

        Define a class named Character.

        It needs an __init__ method that initializes three instance attributes:

            name (String)

            hp (Integer: Health Points)

            strength (Integer: How hard they hit)

        Bonus/Best Practice: Add a __str__ method so that when we print(character_instance), it shows us a nice string format like "Hero (HP: 100)" instead of <__main__.Character object at 0x00... >.

    Sanity Check (main.py):

        In main.py, import the Character class from models.py.

        Instantiate a character (e.g., a "Hero" with 100 HP and 10 Strength).

        Print that character to the console to verify everything is hooked up correctly.

Acceptance Criteria:

    Running python main.py in your terminal prints the character's details without crashing.