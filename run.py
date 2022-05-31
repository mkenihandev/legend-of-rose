# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


import time


class Room(object):
    """
    Creates instance of Room
    """
    def __init__(self, name, inventory, size):
        self.name = name
        self.inventory = inventory
        self.size = size

    def remove_item(self, item):
        self.inventory.remove(item)

    def get_inventory(self):
        print('\nLooking around you see: \n')
        for item in self.inventory:
            if isinstance(item, str):
                print(f'- A {item}')
            else:
                print(f'- A {item.name}')

    def description(self):
        print(f'A {self.size} room, dimly lit.')


class Weapon(object):
    """
    Creates instance of Weapon
    """
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def attack(self):
        return self.damage


hands = Weapon('Hands', 10)

torch = Weapon('Torch', 15)

sword = Weapon('Sword', 35)

axe = Weapon('Axe', 50)

bomb = Weapon('Bomb', 100)


class Human(object):
    """
    Creates instance of Human
    """
    def __init__(self, name, health):
        self.name = name
        self.health = health


class Player(object):
    """
    Creates and instance of Player
    """
    def __init__(self, name, health, inventory, equipped):
        self.name = name
        self.health = health
        self.inventory = inventory
        self.equipped = equipped  # Equipped Weapon

    def get_inventory(self):
        if self.inventory == []:
            print('\nYou have nothing in your inventory')
        else:
            for item in self.inventory:
                if isinstance(item, str):
                    print(f'- A {item}')
                else:
                    print(f'- A {item.name}')

    def update_inventory(self, item):
        self.inventory.append(item)

    def attack(self, target):
        if target.health > 0:
            print(f'\nYou attack the {target.name}')
            target.health -= self.equipped.attack()
            print(f"\nYou deal {self.equipped.damage} damage to the {target.name}")
        else:
            print(f"\nStop!!! {target.name}'s already dead 😭")

    def equip(self, item):
        """
        Equips an item from the players inventory
        Checks if item is in inventory first
        """
        is_in = False

        for x in self.inventory:
            if item.lower() in x.name.lower():
                self.equipped = x
                is_in = True
                break

        if is_in:
            print(f'You have equipped the {x.name}')
        else:
            print(f'You do not have the {item}')

    def unequip(self):
        self.equipped = hands


bandit = Human('Bandit', 100)

cellar = Room('Cellar', [torch], 'small')

player = Player("sanct", 100, [axe, sword, torch], hands)


def loop_back(room):
    """
    Takes the current room as a parameter and loops it back
    Created to allow functions like check_generics() to exist outside
    of the scenarios and still loop the room back
    """
    room()


def check_generics(choice, room):
    """
    Checks for generic choices the player can do in any scenario/room
    """
    if 'inventory' in choice:
        player.get_inventory()
        loop_back(room)
    elif 'look around' in choice:
        room.get_inventory()
        loop_back(room)
    elif 'equip' in choice:
        equipment = input('\nWhat item would you like to equip?\n')
        player.equip(equipment)
        loop_back(room)
    elif 'quit' in choice:
        quit()
    else:
        pass


# def scene_one():
#     print("""
#     What do you do?
#     (E.g. Look around/Open Door/Inventory)
#     """)
#     answer = ''
#     while (answer == ''):
#         answer = input('\n').lower()
#         if 'look around' in answer and torch not in player.inventory:
#             cellar.get_inventory()
#             time.sleep(2)
#             scene_one()
#         elif answer == 'look around' and torch in player.inventory:
#             print('\nYou see the soot from where the torch used to be.')
#             time.sleep(2)
#             scene_one()
#         elif 'torch' in answer and torch not in player.inventory:
#             print('\nYou pick up the torch.')
#             player.update_inventory(torch)
#             time.sleep(2)
#             scene_one()
#         elif answer == 'inventory':
#             player.get_inventory()
#             time.sleep(2)
#             scene_one()
#         elif 'equip' in answer:
#             pickup = input('\nWhat item would you like to equip?\n')  # issues here, need non string to compare it to inventory items
#             player.equip(pickup)
#             scene_one()
#         elif answer == 'stay here':
#             print('\nYou patiently wait and die of hunger. Please restart.')
#             break
#         elif answer == 'quit':
#             print('\nThe Rose awaits your next attempt.')
#             break
#         elif answer == 'open door':
#             print('Next Scene')
#             break
#         else:
#             print('\nYou cannot do that.')
#             time.sleep(2)
#             scene_one()


# print("""
# Welcome Hero to The Legend of Rose.
# Your goal is to obtain the legendary Rose held in Castle Rosebush.
# Revered for it's incredible ability to flatter the one you love, 
# it is well guarded.
# You will face many challenges along the way, and the choices you make may 
# affect the outcome.\n""")

# time.sleep(2)

# player = Player(input('Enter your name, Hero: '), 100, [], hands)

# time.sleep(2)

# print(f'\nAh, {player.name}, a fine name for a valiant Knight.\n')

# time.sleep(2)

# print("""
#     You stand in a single square room of a sprawling dungeon. 
#     You were told at the end of this dungeon, 
#     a secret passage can be found 
#     leading directly to the throne room of Caslte Rosebush, 
#     where the Rose is held.
#     Ahead of you, there is a door.
#     """)

# scene_one()