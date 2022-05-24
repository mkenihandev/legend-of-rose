# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


class Room(object):
    """
    Creates instance of Room
    """
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory

    def remove_item(self, item):
        self.inventory.remove(item)

    def get_inventory(self):
        print(f'Looking around you see: \n')
        for item in self.inventory:
            print(f'- A {item.name}')


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
        print(self.inventory)

    def update_inventory(self, item):
        self.inventory.append(item)

    def attack(self, target):
        target.health -= self.equipped.attack()

    def equip(self, item):
        if item in self.inventory:
            self.equipped = item
        else:
            print(f'You do not have a {str(item.name)}')

    def unequip(self):
        self.equipped = hands


bandit = Human('Bandit', 100)
player = Player('sanct', 100, [], hands)
cellar = Room('Cellar', [torch, sword, axe])


cellar.get_inventory()
cellar.remove_item(torch)
cellar.get_inventory()


# def good_or_bad():
#     answer = ''
#     while answer != 'yes' and answer != 'no':
#         answer = input(f'A simple choice to start with {player.name}, are you good and true of heart?\nYes/No: ').lower()
#         alignment = ''
#         if answer == 'yes':
#             alignment = 'a stoic Knight, good and true of heart'
#         else:
#             alignment = 'a dark soul, ruthless and out for blood'
#     return alignment


# def scene_one():
#     print("""
#     What do you do?
#     (E.g. Look around/Open Door/Inventory)
#     """)
#     answer = ''
#     while (answer == ''):
#         answer = input('').lower()
#         if answer == 'look around' and 'torch' not in player.inventory:
#             print('You see an unlit torch lying on the ground.')
#             scene_one()
#         elif answer == 'look around' and 'torch' in player.inventory:
#             print('You see the soot from where the torch used to be.')
#             scene_one()
#         elif answer == 'inventory':
#             print('The items in your inventory:')
#             for item in player.inventory:
#                 print(f'- {item}')
#             scene_one()
#         elif answer == 'open door':
#             print('Next Scene')
#             break
#         elif answer == 'stay here':
#             print('You have died. Restart.')
#             break
#         elif 'torch' in answer and 'torch' not in player.inventory:
#             print('You pick up the torch.')
#             player.update_inventory('torch')
#             scene_one()
#         elif answer == 'quit':
#             print('The Rose awaits your next attempt.')
#             break
#         else:
#             print('You cannot do that.')
#             scene_one()


# def scene_two():
#     print(f'While will you do, brave {player.name}?')
#     answer = ''
#     while (answer == ''):
#         answer = input('').lower()
#         if answer == 'attack': 



# print("""
# Welcome Hero to The Legend of Rose.
# Your goal is to obtain the legendary Rose held in Castle Rosebush.
# Revered for it's incredible ability to flatter the one you love, 
# it is well guarded.
# You will face many challenges along the way, and the choices you make may 
# affect the outcome.\n""")

# print(f'\nAh, {player.name}, a fine name for a valiant Knight.\n')

# alignment = good_or_bad()

# print(f'\nYou are {alignment}, interesting.')


# print("""
#     You stand in a single square room of a sprawling dungeon. 
#     You were told at the end of this dungeon, 
#     a secret passage can be found 
#     leading directly to the throne room of Caslte Rosebush, 
#     where the Rose is held.
#     Ahead of you, there is a door.
#     """)


# scene_one()