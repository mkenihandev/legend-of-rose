# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import os
os.system('cls' if os.name == 'nt' else 'clear')


import time


# -------------------------------------------- Classes ---------------------------------


class Room(object):
    """
    Creates instance of Room
    """
    def __init__(self, name, inventory, size, sections):
        self.name = name
        self.inventory = inventory
        self.size = size
        self.sections = sections

    def remove_item(self, item):
        """
        Method for removing an item from the rooms item pool
        """
        self.inventory.remove(item)

    def get_inventory(self):
        """
        Prints out the rooms inventory
        """
        if self.inventory == []:
            pass
        else:
            print('\nLooking around you see: \n')
            for item in self.inventory:
                if isinstance(item, str):
                    print(f'- A {item}')
                else:
                    print(f'- A {item.name}')

    def description(self):
        """
        Describes the room
        """
        print(f'\nA {self.size} room, seemingly has {self.sections} sections.')


class Weapon(object):
    """
    Creates instance of Weapon
    """
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def attack(self):
        """
        Returns the damage number from the weapon for use elsewhere
        """
        return self.damage


class Item(object):
    """
    Creates instance of Item
    """
    def __init__(self, name, modifier):
        self.name = name
        self.modifier = modifier


class Human(object):
    """
    Creates instance of Human
    """
    def __init__(self, name, health, turn):
        self.name = name
        self.health = health
        self.turn = turn


# ---------------------------------------- Player Class ---------------------------------


class Player(object):
    """
    Creates and instance of Player
    """

    def __init__(self, name, health, max_health, inventory, equipped, turn, current_room):
        self.name = name
        self.health = health
        self.inventory = inventory
        self.equipped = equipped  # Equipped Weapon
        self.turn = turn
        self.max_health = max_health
        self.current_room = current_room

    def get_inventory(self):
        """
        Prints everything in player inventory
        """
        if self.inventory == []:
            print('\nYou have nothing in your inventory')
        else:
            for item in self.inventory:
                if isinstance(item, str):
                    print(f'- A {item}')
                else:
                    print(f'- A {item.name}')

    def update_inventory(self, item):
        """
        Adds an item to the players inventory
        """
        self.inventory.append(item)

    def attack(self, target):
        """
        Attack method, takes a target and applies damage using equipped weapon value
        """
        if target.health > 0:
            print(f'\nYou attack the {target.name} with your {self.equipped.name}')
            target.health -= self.equipped.attack()
            time.sleep(1)
            print(f"\nYou deal {self.equipped.damage} damage to the {target.name}")
        else:
            print(f"\nStop!!! {target.name}'s already dead 😭")

    def pickup(self, item):
        if item in self.current_room.inventory:
            self.update_inventory(item)
            self.current_room.remove_item(item)
        else:
            print('You already have that.')

    def equip(self, item):
        """
        Equips an item from the players inventory
        Checks if item is in inventory first
        """
        is_in = False

        for x in self.inventory:
            if item.lower() in x.name.lower():
                self.update_inventory(self.equipped)
                self.equipped = x
                is_in = True
                break

        if is_in:
            print(f'\nYou have equipped the {x.name}')
        else:
            print(f'\nYou do not have the {item}')

    def unequip(self):
        """
        Unequips held weapon and defaults to hands
        """
        self.equipped = hands

    def heal(self):
        """
        Heals the player if there is a potion in their inventory
        """
        if potion in self.inventory:
            if self.health <= 80:
                self.health += potion.modifier
                print(f'\nYou have healed for {potion.modifier} points! Your health is now {self.health}')
                self.inventory.remove(potion)
            elif self.health > 80 and self.health != 100:
                health_to_add = (100 - self.health)
                self.health += health_to_add
                print(f'\nYou have healed for {health_to_add} points! Your health is now {self.health}')
                self.inventory.remove(potion)
            elif self.health == self.max_health:
                print('\nYou are already max health.')
        else: 
            print('\nYou do not have a health potion.')


# ---------------------------------------- Base functions ---------------------------------


def loop_back(player, scene):
    """
    Takes the current room as a parameter and loops it back
    Created to allow functions like check_generics() to exist outside
    of the scenarios and still loop the room back
    """
    scene(player)


def check_generics(player, choice, room, scene):
    """
    Checks for generic choices the player can do in any scenario/room
    """
    if 'inventory' in choice:
        os.system('clear')
        player.get_inventory()
        time.sleep(1)
        loop_back(player, scene)
    elif 'look around' in choice:
        os.system('clear')
        room.description()
        room.get_inventory()
        time.sleep(1)
        loop_back(player, scene)
    elif 'equip' in choice:
        os.system('clear')
        equipment = input('\nWhat item would you like to equip?\n')
        player.equip(equipment)
        time.sleep(1)
        loop_back(player, scene)
    elif 'quit' in choice:
        quit()
    else:
        pass


def menu():
    """
    Menu for the game, gives player chance to learn about the game before hopping in
    """
    menu = True
    while menu:
        os.system('clear')
        print("""
Welcome Hero to The Legend of Rose.
Your goal is to obtain the legendary Rose held in Castle Rosebush.
Revered for it's incredible ability to flatter the one you love, 
it is well guarded.
You will face many challenges along the way, and the choices you make may 
affect the outcome.\n""")
        print("""
Type the corrosponding letter to choose:
P - Play
I - Information
        """)
        answer = ''
        while (answer == ''):
            answer = input('').lower()
            if 'p' in answer or 'play' in answer:
                menu = False
            elif 'i' in answer or 'information' in answer:
                print("""
Play The Legend of Rose by typing whatever you like at given points.
The system will determine if your input is valid and let you do certain 
actions.
If there is something you cannot do, the system should tell you this.
Combat is taken in turns with the AI.
The story is silly and not to be taken seriously, get silly with it!
                """)
                time.sleep(3)
                print("Back to Menu? (Any input)")
                input('')

# --------------------------------------- Combat ---------------------------------


def combat(player, enemy):
    """
    Combat function, does not break until player/ai hp is 0
    """
    while player.health and enemy.health > 0:
        if player.turn:
            print(f'The {enemy.name} is in front of you. What do you do?')
            user_answer = input('\n').lower()

            check_generics(player, user_answer, player.current_room, scene_one)

            if 'attack' in user_answer:
                player.attack(enemy)
                print(f'{enemy.name} health is now {enemy.health}')
                player.turn = False
            elif 'heal' in user_answer:
                player.heal()
                player.turn = False
            elif 'kiss' in user_answer:
                print(f'You kiss the {enemy.name}, for a brief second they fall in love with you. As a consequence they take some damage and lose a turn.')
                enemy.health -= 10
                print(f'{enemy.name} health is now {enemy.health}')
                player.turn = True
        else:
            damage = 10
            print(f'\nThe {enemy.name} attacks you for {damage} health')
            player.health -= damage
            time.sleep(1)
            print(f'\nYour health is now {player.health}')
            player.turn = True


# --------------------------------------- Object definitions ---------------------------------

hands = Weapon('Hands', 10)

torch = Weapon('Torch', 15)

sword = Weapon('Sword', 35)

axe = Weapon('Axe', 50)

bomb = Weapon('Bomb', 100)

potion = Item('Health Potion', 20)

armor = Item('Armor', 50)

bandit = Human('Bandit', 100, False)

cellar = Room('Cellar', [torch], 'small', 3)


# --------------------------------------- Main Game Scenarios ---------------------------------


def scene_one(player):
    """
    First scene, cellar
    """
    print("""
    What do you do?
    (E.g. Look around/Open Door/Inventory)
    """)
    answer = ''
    while (answer == ''):
        answer = input('\n').lower()
        check_generics(player, answer, cellar, scene_one)
        if answer == 'stay here':
            print('\nYou patiently wait and die of hunger. Please restart.')
            quit()
        elif answer == 'open door':
            print('Next Scene')
            break
        elif 'torch' in answer:
            player.pickup(torch)
            scene_one(player)
        else:
            print('\nYou cannot do that.')
            time.sleep(2)
            scene_one(player)

# --------------------------------------- Main Game ---------------------------------


def main():
    """
    Main game function
    """
    # menu()
    # os.system('clear')
    player = Player(input('\nWhat is your name, Hero?'), 80, 100, [], hands, True, cellar)
    # print(f'\nAh, {player.name}, a fine name for a budding adventurer.')
    # time.sleep(2)
#     print("""\nYou find yourself in a dimly lit cellar.
# You have been told this cellar leads to a secret passage directly to the Throne Room
# of Castle Rose.
# Ahead of you lies a single door... but perhaps you should look around first?""")
    scene_one(player)


main()