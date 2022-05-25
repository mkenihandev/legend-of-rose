# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


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
        if target == 'ladybug':
            print("""You attack the ladybug.
You absolute Monster. 
The ladybug releases a deadly neurotoxin that immediately kills you. 
You have died.""")
        elif target.health > 0:
            print(f'\nYou attack the {target.name}')
            target.health -= self.equipped.attack()
            print(f"\nYou deal {self.equipped.damage} damage to the {target.name}")
        else:
            print(f"\nStop!!! {target.name}'s already dead 😭")

    def equip(self, item):
        if item in self.inventory:
            self.equipped = item
        else:
            print(f'\nYou do not have a {str(item.name)}')

    def unequip(self):
        self.equipped = hands


bandit = Human('Bandit', 100)
cellar = Room('Cellar', [torch, bandit, 'ladybug'], 'small')


def scene_one():
    print("""
    What do you do?
    (E.g. Look around/Open Door/Inventory)
    """)
    answer = ''
    while (answer == ''):
        answer = input('').lower()
        if 'look around' in answer and torch not in player.inventory:
            cellar.get_inventory()
            scene_one()
        elif answer == 'look around' and torch in player.inventory:
            print('\nYou see the soot from where the torch used to be.')
            scene_one()
        elif 'torch' in answer and torch not in player.inventory:
            print('\nYou pick up the torch.')
            player.update_inventory(torch)
            scene_one()
        elif answer == 'inventory':
            player.get_inventory()
            scene_one()
        elif answer == 'stay here':
            print('\nYou patiently wait and die of hunger. Please restart.')
            break
        elif answer == 'quit':
            print('\nThe Rose awaits your next attempt.')
            break
        elif answer == 'open door':
            print('Next Scene')
            break
        else:
            print('\nYou cannot do that.')
            scene_one()


# def scene_two():
#     print(f'While will you do, brave {player.name}?')
#     answer = ''
#     while (answer == ''):
#         answer = input('').lower()
#         if answer == 'attack': 


print("""
Welcome Hero to The Legend of Rose.
Your goal is to obtain the legendary Rose held in Castle Rosebush.
Revered for it's incredible ability to flatter the one you love, 
it is well guarded.
You will face many challenges along the way, and the choices you make may 
affect the outcome.\n""")

player = Player(input('Enter your name, Hero: '), 100, [], hands)

print(f'\nAh, {player.name}, a fine name for a valiant Knight.\n')

print("""
    You stand in a single square room of a sprawling dungeon. 
    You were told at the end of this dungeon, 
    a secret passage can be found 
    leading directly to the throne room of Caslte Rosebush, 
    where the Rose is held.
    Ahead of you, there is a door.
    """)

scene_one()