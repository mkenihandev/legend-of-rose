# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import time

import os
os.system('cls' if os.name == 'nt' else 'clear')


# -------------------------------------------- Classes -----------------------


class Room(object):
    """
    Creates instance of Room
    """
    def __init__(self, name, inventory, size, sections, flavor):
        self.name = name
        self.inventory = inventory
        self.size = size
        self.sections = sections
        self.flavor = flavor

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
        print(f'\n{self.flavor}')


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


class Enemy(object):
    """
    Creates instance of Enemy
    """
    def __init__(self, name, health, damage, turn, loot):
        self.name = name
        self.health = health
        self.damage = damage
        self.turn = turn
        self.loot = loot

    def get_loot(self):
        """
        Prints everything in enemy inventory
        """
        if self.loot == []:
            print('nothing.')
        else:
            for item in self.loot:
                if isinstance(item, str):
                    print(f'- A {item}')
                else:
                    print(f'- A {item.name}')


# ------------------------ Player Class ----------------------


class Player(object):
    """
    Creates and instance of Player
    """

    def __init__(self, name, health, max_health, inventory,
                 equipped, turn, current_room):
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
        Attack method, takes a target and applies damage using
        equipped weapon value
        """
        if target.health > 0:
            print(f'\nYou attack the {target.name} '
                  f'with your {self.equipped.name}')
            target.health -= self.equipped.attack()
            time.sleep(1)
            print(f"\nYou deal {self.equipped.damage} "
                  f"damage to the {target.name}")
        else:
            print(f"\nStop!!! {target.name}'s already dead 😭")

    def pickup(self, item, room):
        """
        Checks room inventory for the item before allowing pickup of item
        """
        print(f'\nYou pick up the {item.name}')
        self.update_inventory(item)
        room.remove_item(item)

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
                print(f'\nYou have healed for {potion.modifier} points!'
                      f'Your health is now {self.health}')
                self.inventory.remove(potion)
            elif self.health > 80 and self.health != 100:
                health_to_add = (100 - self.health)
                self.health += health_to_add
                print(f'\nYou have healed for {health_to_add} points!'
                      f'Your health is now {self.health}')
                self.inventory.remove(potion)
            elif self.health == self.max_health:
                print('\nYou are already max health.')
        else:
            print('\nYou do not have a health potion.')


# --------------------------- Base functions ------------------


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
        player.get_inventory()
        time.sleep(3)
        loop_back(player, scene)
    elif 'look' in choice:
        room.description()
        room.get_inventory()
        time.sleep(3)
        loop_back(player, scene)
    elif 'pick up' in choice:
        for item in room.inventory:
            player.pickup(item, room)
        if room.inventory == []:
            print('There is nothing left in the room')
        loop_back(player, scene)
    elif 'equip' in choice:
        os.system('clear')
        equipment = input('\nWhat item would you like to equip?\n')
        player.equip(equipment)
        time.sleep(1)
        loop_back(player, scene)
    elif 'quit' in choice:
        quit()


def menu():
    """
    Menu for the game, gives player chance to learn about the game before
    hopping in
    """
    menu_screen = True
    while menu_screen:
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
        while answer == '':
            answer = input('').lower()
            if 'p' in answer or 'play' in answer:
                menu_screen = False
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

# --------------------------------------- Combat ----------------------------


def combat(player, enemy, scene):
    """
    Combat function, does not break until player/ai hp is 0
    """
    while player.health and enemy.health > 0:
        if player.turn:
            print(f'\nThe {enemy.name} is in front of you. What do you do?')
            user_answer = input('\n').lower()

            os.system('clear')

            check_generics(player, user_answer, player.current_room, scene)

            if 'attack' in user_answer:
                player.attack(enemy)
                print(f'\n{enemy.name} health is now {enemy.health}')
                player.turn = False
            elif 'heal' in user_answer:
                player.heal()
                player.turn = False
        else:
            damage = enemy.damage
            print(f'\nThe {enemy.name} attacks you for {damage} health')
            player.health -= damage
            time.sleep(1)
            print(f'\nYour health is now {player.health}')
            player.turn = True

    if player.health > 0 and enemy in player.current_room.inventory:
        player.turn = True
        print(f'\nYou defeated the {enemy.name}, congratulations!')
        print('They drop:')
        enemy.get_loot()
        for items in enemy.loot:
            player.current_room.inventory.append(items)  # adds loot from
# enemy to room pool
        player.current_room.remove_item(enemy)  # removes the enemy from
# room pool
    elif player.health <= 0:
        print('You have died. Restart.')
    else:
        pass


# -------------- Object definitions -----------------

hands = Weapon('Hands', 10)

torch = Weapon('Torch', 15)

sword = Weapon('Sword', 35)

axe = Weapon('Axe', 50)

excalibur = Weapon('Excalibur', 75)

bomb = Weapon('Bomb', 100)

potion = Item('Health Potion', 35)

armor = Item('Armor', 50)

injured_bandit = Enemy('Injured Bandit', 10, 10, False, [potion, sword])

bandit = Enemy('Bandit', 10, 15, False, [potion, bomb])

fat_bandit = Enemy('Fat Bandit', 10, 20, False, [armor])

small_ogre = Enemy('Small Ogre', 100, 30, False, [axe, potion, potion])

mother_ogre = Enemy('Mother Ogre', 150, 45, False,
                    [potion, potion, potion, bomb])

final_boss = Enemy('Mergo, Guardian of the Rose', 300, 60, False, [])

cellar = Room('Cellar', [torch, potion, potion, potion, potion], 'small', 1,
              '\nThe room is dimly lit by something.')

storage = Room('Storage Room', [injured_bandit, potion], 'small', 1,
               "\nAt the back of the room there appears"
               " to be a shattered wall,"
               "\nleading to a passage")

dungeon = Room('Dungeon', [bandit, potion, potion], 'small', 1,
               "\nThe dungeon reeks of various different bodily fluids."
               "\nPerhaps it's best you don't ask."
               "\nAhead you see the stairs out,"
               " but to the left a board covering the entrance to"
               " some side room.")

dining_hall_one = Room('Foyer Entrance', [fat_bandit], 'medium', 2,
                       "The Foyer opens up to reveal a sizeable room,"
                       "seperated seemingly in half by a large curtain.")

# ------------------------ Main Game Scenarios ----------------


def scene_one(player):
    """
    First scene, cellar
    """
    player.current_room = cellar
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
            os.system('clear')
            scene_two(player)
        elif 'torch' in answer:
            player.pickup(torch)
            scene_one(player)
        else:
            print('\nYou cannot do that.')
            time.sleep(2)
            scene_one(player)


def scene_two(player):
    """
    Second scene, storage room
    """
    print("""\nYou open the door to the storage room.""")
    if injured_bandit in storage.inventory:
        print("""\nAt first, everything seems normal, but suddenly an injured
        bandit approaches you.
'That Rose is mine, Hero, give it 'ere'""")
    else:
        pass
    player.current_room = storage
    combat(player, injured_bandit, scene_two)
    print('What do you do?')
    answer = ''
    while (answer == ''):
        answer = input('\n').lower()
        check_generics(player, answer, storage, scene_two)  # Add picking up
        # ability
        if 'wall' in answer:
            print("""\nYou break down the fragile wall to reveal a
passage to a large dungeon.
You get the eery feeling you're in for it now.""")
            scene_three(player)
        elif 'back' in answer:
            print('You make your way back to the previous room')
            scene_one(player)
        elif 'potion' in answer:
            player.pickup(potion)
            scene_two(player)
        else:
            print('\nYou cannot do that.')
            time.sleep(2)
            scene_two(player)


def scene_three(player):
    """
    Third Scene, dungeon, small again but side room too
    """
    player.current_room = dungeon
    print("""\nYou enter what seems to be an old torture chamber.
Partially regretting ever setting out on this mission you step a ways in.""")
    if bandit in dungeon.inventory:
        print("From behind one of the various horrific devices,"
              " a Bandit jumps out and swiped at you."
              "He missed, but you know there's no talking your"
              " way out of this one.")
    else:
        pass
    combat(player, bandit, scene_three)
    print('What will you do?')
    answer = ''
    while (answer == ''):
        answer = input('\n').lower()
        check_generics(player, answer, dungeon, scene_three)
        if 'stairs' in answer:
            print("""\nYou approach the stairs and climb it step by step.
What you see at the top seems to be the Dining Hall for castle staff.
A foul smell fills the air, something has been living here...""")
            quit()
        elif 'board' in answer:
            print("""\nYou move the board out of the way and step inside.
It appears to be a room for stashing the various pieces of armor from the
aforementioned bodies.
A bunch of clothes and broken armor spill out on to the floor.""")
            player.current_room.inventory.append(armor)
            player.current_room.inventory.append(potion)
            player.current_room.inventory.append(bomb)
        elif 'back' in answer:
            print('\nYou make your way back to the previous room')
            scene_two(player)
        else:
            print('\nYou cannot do that.')
            time.sleep(2)
            scene_three(player)


def scene_four_sect_one(player):
    """
    Scene four, medium room with two sections, side room
    """
    player.current_room = dining_hall_one
    if fat_bandit in dining_hall_one.inventory:
        print("A very large bandit sitting at one of the many tables,"
              " looks up from the meal he was eating directly at you")
    else:
        pass
    combat(player, bandit, scene_four_sect_one)


# --------------------------------------- Main Game --------------------------


def main():
    """
    Main game function
    """
    menu()
    os.system('clear')
    player = Player(input('\nWhat is your name, Hero?\n'), 100, 100, [],
                    hands, True, cellar)
    print(f'\nAh, {player.name}, a fine name for a budding adventurer.')
    time.sleep(2)
    print("""\nYou find yourself in a dimly lit cellar.
You have been told this cellar leads to a secret passage
directly to the Throne Room of Castle Rose.
Ahead of you lies a single door... but perhaps you should
look around first?""")
    time.sleep(2)
    scene_one(player)


main()
