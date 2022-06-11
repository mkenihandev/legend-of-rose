"""
This module is the Legend of Rose game in its entirety,
from classes to scenarios
"""

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
    def __init__(self, name, damage, class_name):
        self.name = name
        self.damage = damage
        self.class_name = class_name

    def attack(self):
        """
        Returns the damage number from the weapon for use elsewhere
        """
        return self.damage


class Item(object):
    """
    Creates instance of Item
    """
    def __init__(self, name, modifier, class_name):
        self.name = name
        self.modifier = modifier
        self.class_name = class_name


class Enemy(object):
    """
    Creates instance of Enemy
    """
    def __init__(self, name, health, damage, loot, class_name):
        self.name = name
        self.health = health
        self.damage = damage
        self.loot = loot
        self.class_name = class_name

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
                 equipped, turn, current_room, good_person,
                 board_used, key_used):
        self.name = name
        self.health = health
        self.inventory = inventory
        self.equipped = equipped  # Equipped Weapon
        self.turn = turn
        self.max_health = max_health
        self.current_room = current_room
        self.good_person = good_person
        self.board_used = board_used
        self.key_used = key_used

    def get_inventory(self):
        """
        Prints everything in player inventory
        """
        if self.inventory == []:
            print('\nYou have nothing in your inventory')
            print(f'\nYour equipped weapon is: {self.equipped.name}')
            print(f'Your current health is: {self.health}')
            print(f'Your max health is: {self.max_health}')
        else:
            for item in self.inventory:
                if isinstance(item, str):
                    print(f'- A {item}')
                else:
                    print(f'- A {item.name}')
            print(f'\nYour equipped weapon is: {self.equipped.name}')
            print(f'Your current health is: {self.health}')
            print(f'Your max health is: {self.max_health}')

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
            if self.equipped == bomb:
                print(f'\nYou attack the {target.name} '
                      f'with your {self.equipped.name}')
                target.health -= self.equipped.attack()
                time.sleep(1)
                print(f"\nYou deal {self.equipped.damage} "
                      f"damage to the {target.name}")
                self.inventory.remove(bomb)
                self.equipped = hands
            else:
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
        is_tool_enemy = False

        for x_item in self.inventory:
            if item.lower() in x_item.name.lower():
                if x_item.class_name == 'enemy' or x_item.class_name == 'tool':
                    print('\nYou cannot equip this item.')
                    is_tool_enemy = True
                elif x_item.class_name == 'armor':
                    self.max_health += 50
                    self.inventory.remove(armor)
                    is_in = True
                    break
                else:
                    self.equipped = x_item
                    is_in = True
                    break

        if is_in:
            print(f'\nYou have equipped the {x_item.name}')
        elif is_tool_enemy:
            pass
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
            if self.health <= (self.max_health - 40):
                # Heals for the max amount a potion can
                print('\nYou drink a potion, it tastes bitter.')
                self.health += 40
                self.inventory.remove(potion)
                print(f'\nYour health is now {self.health}')
            elif self.health > (self.max_health - 40):
                # To prevent the user going over the max health
                print('\nYou drink a potion, it tastes bitter.')
                to_heal = self.max_health - self.health
                self.health += to_heal
                self.inventory.remove(potion)
                print(f'\nYour health is now {self.health}')
            else:
                print('Something borked')
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
    if 'inventory' in choice or 'backpack' in choice:
        os.system('clear')
        player.get_inventory()
        time.sleep(2)
        loop_back(player, scene)
    elif 'look' in choice or 'search' in choice or 'survey' in choice:
        os.system('clear')
        room.description()
        room.get_inventory()
        time.sleep(2)
        loop_back(player, scene)
    elif 'pick' in choice or 'loot' in choice or 'grab' in choice:
        if room.inventory == []:
            print('\nThere is nothing left in the room')
        else:
            player.inventory.extend(room.inventory)
            print('\nYou pick up all the items currently in the room')
            room.inventory = []
        loop_back(player, scene)
    elif 'equip' in choice or 'hold' in choice:
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
actions. (E.g. "attack", "look around", "break down wall")
If there is something you cannot do, the system should tell you this.
Combat is taken in turns with the AI.
Refer to the README for some guidance on actions you can take.""")
                time.sleep(3)
                print("\nBack to Menu? (Any input)")
                input('')

# --------------------------------------- Combat ----------------------------


def combat(player, enemy, scene):
    """
    Combat function, does not break until player/ai hp is 0
    """
    while player.health > 0 and enemy.health > 0:
        if player.turn:
            print(f'\nThe {enemy.name} is in front of you. What do you do?')
            user_answer = input('\n').lower()

            os.system('clear')

            check_generics(player, user_answer, player.current_room, scene)

            if 'attack' in user_answer or 'hit' in user_answer:
                player.attack(enemy)
                print(f'\n{enemy.name} health is now {enemy.health}')
                player.turn = False
            elif 'heal' in user_answer or 'potion' in user_answer:
                player.heal()
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
        print('You have died. Restart!')
        quit()
    else:
        pass


# -------------- Object definitions -----------------

hands = Weapon('Hands', 5, 'weapon')

torch = Weapon('Torch', 10, 'weapon')

sword = Weapon('Sword', 20, 'weapon')

axe = Weapon('Axe', 45, 'weapon')

excalibur = Weapon('Excalibur', 75, 'weapon')

bomb = Weapon('Bomb', 100, 'weapon')

potion = Item('Health Potion (+40 hp)', 40, 'tool')

armor = Item('Piece of Armor (+50 hp when equipped)', 50, 'armor')

key = Item('Key', 0, 'tool')

note = Item('A note that reads: "Save your bombs for the end"', 0, 'tool')

injured_bandit = Enemy('Injured Bandit', 15, 10, [potion], 'enemy')

bandit = Enemy('Bandit', 30, 15, [bomb, sword], 'enemy')

fat_bandit = Enemy('Fat Bandit', 50, 20, [armor], 'enemy')

small_ogre = Enemy('Small Ogre', 100, 25, [key, axe, potion], 'enemy')

mother_ogre = Enemy('Mother Ogre', 150, 45, [potion, potion, potion, bomb],
                    'enemy')

final_boss = Enemy('Guardian of the Rose', 600, 60, [], 'enemy')

cellar = Room('Cellar', [torch], 'small', 1,
              '\nThe room is dimly lit by something.')

storage = Room('Storage Room', [injured_bandit, potion], 'small', 1,
               "\nAt the back of the room there appears"
               " to be a shattered wall,"
               "\nleading to a passage")

dungeon = Room('Dungeon', [bandit, potion], 'small', 1,
               "\nThe dungeon reeks of various different bodily fluids."
               "\nPerhaps it's best you don't ask."
               "\nAhead you see the stairs out,"
               " but to the left a board covering the entrance to"
               " some side room.")

dining_hall_one = Room('Dining Hall Entrance', [fat_bandit], 'medium', 2,
                       "The Foyer opens up to reveal a sizeable room,"
                       "seperated seemingly in half by a large curtain.")

dining_hall_two = Room('Dining Hall Kitchen', [small_ogre], 'medium',
                       2, 'The Kitchen is host to a sizeable amount'
                       ' of animal carcasses. Seems something has been feeding'
                       ' here.'
                       "There appears to be a stairway to the Castle's main"
                       " hall at the back of the room... but to the side a"
                       " door. It appears to be locked."
                       "Perhaps if you had a key?")

main_hall_one = Room('Main Hall Foyer', [mother_ogre], 'large', 3,
                     'The Foyer of the Main Hall is lined with corpses of'
                     ' heroes and bandits alike.'
                     'The Foyer appears to have a gigantic stairway,'
                     ' that leads up to the Throne Room. Something seems to'
                     ' be halfway up the stairs.')

main_hall_two = Room('Main Hall Stairway', [], 'large', 3,
                     'Deceivingly high up, you can see the Foyer could have'
                     ' been host to multiple hundreds of people. The Throne'
                     ' Room still awaits you up the rest of the stairs.'
                     'There is a bonfire lit here, with an odd sword stuck'
                     ' in it. The bonfire makes you feel safe.')

main_hall_two_v2 = Room('Main Hall Stairway', [], 'large', 3,
                        'Deceivingly high up, you can see the Foyer could have'
                        ' been host to multiple hundreds of people. The Throne'
                        ' Room still awaits you up the rest of the stairs.'
                        'There is a bonfire lit here, the legendary sword now'
                        ' missing from it. The bonfire makes you feel safe.')

main_hall_three = Room('Throne Room', [final_boss], 'large', 3,
                       'The Throne Room has a sinister aura. You can see the'
                       ' Rose sitting just out of reach. Your quests end'
                       ' draws near')

# ------------------------ Main Game Scenarios ----------------


def scene_one(player):
    """
    First scene, cellar
    """
    player.current_room = cellar
    print("""
[Cellar] What do you do?
(E.g. Look around/Open Door/Inventory)
    """)
    answer = ''
    while answer == '':
        answer = input('\n').lower()
        check_generics(player, answer, cellar, scene_one)
        if 'stay' in answer:
            print('\nYou patiently wait and die of hunger. Please restart.')
            quit()
        elif 'open' in answer or 'door' in answer or 'forward' in answer:
            os.system('clear')
            scene_two(player)
        else:
            print('\nYou cannot do that.')
            time.sleep(2)
            scene_one(player)


# ------------------------ Scene Two ----------------


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
    time.sleep(1)
    player.current_room = storage
    combat(player, injured_bandit, scene_two)
    print('\n[Storage Room] What do you do?')
    answer = ''
    while answer == '':
        answer = input('\n').lower()
        check_generics(player, answer, storage, scene_two)  # Add picking up
        # ability
        if 'wall' in answer or 'break' in answer:
            print("""\nYou break down the fragile wall to reveal a
passage to a large dungeon.
You get the eery feeling you're in for it now.""")
            scene_three(player)
        elif 'back' in answer:
            print('You make your way back to the previous room')
            scene_one(player)
        else:
            print('\nYou cannot do that.')
            time.sleep(2)
            scene_two(player)


# ------------------------ Scene Three ----------------


def scene_three(player):
    """
    Third Scene, dungeon, small again but side room too
    """
    player.current_room = dungeon
    print("""\nYou enter what seems to be an old torture chamber.
Partially regretting ever setting out on this mission you step a ways in.""")
    time.sleep(2)
    if bandit in dungeon.inventory:
        print("\nFrom behind one of the various horrific devices,"
              " a Bandit jumps out and swipes at you."
              " He missed, but you know there's no talking your"
              " way out of this one.")
    else:
        pass
    combat(player, bandit, scene_three)
    print('\n[Dungeon] What will you do?')
    answer = ''
    while answer == '':
        answer = input('\n').lower()
        check_generics(player, answer, dungeon, scene_three)
        if 'stairs' in answer or 'up' in answer:
            print("""\nYou approach the stairs and climb it step by step.
What you see at the top seems to be the Dining Hall for castle staff.
A foul smell fills the air, something has been living here...""")
            scene_four_sect_one(player)
        elif 'board' in answer or 'move' in answer:
            if not player.board_used:
                os.system('clear')
                print("""\nYou move the board out of the way to reveal a broom closet.
    It appears to be a room for stashing the various pieces of armor from the
    aforementioned bodies.
    A bunch of clothes and broken armor spill out on to the floor.""")
                player.current_room.inventory.append(armor)
                player.current_room.inventory.append(potion)
                player.current_room.inventory.append(bomb)
                player.board_used = True
                scene_three(player)
            else:
                print('You already attained the loot behind the board.')
        elif 'back' in answer:
            print('\nYou make your way back to the previous room')
            scene_two(player)
        else:
            print('\nYou cannot do that.')
            time.sleep(2)
            scene_three(player)


# ------------------------ Scene Four ----------------


def scene_four_sect_one(player):
    """
    Scene four, medium room with two sections,
    side room not accessible from section one
    """
    player.current_room = dining_hall_one
    if fat_bandit in dining_hall_one.inventory:
        print("\nA very large bandit sitting at one of the many tables,"
              " looks up from the meal he was eating directly at you."
              " He still looks hungry.")
    else:
        pass
    combat(player, fat_bandit, scene_four_sect_one)
    print('\n[Dining Hall] What will you do?')
    answer = ''
    while answer == '':
        answer = input('\n').lower()
        check_generics(player, answer, dining_hall_one, scene_four_sect_one)
        if 'curtain' in answer or 'draw' in answer or 'move':
            print('You draw the curtain back to reveal the kitchen.'
                  'Rotten food in various states of eaten is littered'
                  ' just about everywhere.')
            scene_four_sect_two(player)
        elif 'back' in answer:
            print('\nYou make your way back to the previous room')
            scene_three(player)
        else:
            print('\nYou cannot do that.')
            time.sleep(2)
            scene_four_sect_one(player)


def scene_four_sect_two(player):
    """
    Scene four, medium room with two sections.
    side room accesible in this section
    """
    player.current_room = dining_hall_two
    if small_ogre in dining_hall_two.inventory:
        print('\nA small, yet towering Ogre turns from the corner it was'
              " feeding in. Seems you're it's next meal.")
    else:
        pass
    combat(player, small_ogre, scene_four_sect_two)
    print('\n[Dining Hall Kitchen] What do you do?')
    answer = ''
    while answer == '':
        answer = input('\n').lower()
        check_generics(player, answer, dining_hall_two, scene_four_sect_two)
        if 'stairs' in answer or 'up' in answer:
            print('You exit the kitchen and climb the stairs.'
                  ' You have reached the main hall.')
            finale_sect_one(player)
        elif 'door' in answer or 'open' in answer:
            if key in player.inventory and not player.key_used:
                print('\nYou push and twist the key in to the keyhole...')
                time.sleep(1)
                print('\nA hefty amount of loot spills out on the floor')
                dining_hall_two.inventory.append(bomb)
                dining_hall_two.inventory.append(note)
                dining_hall_two.inventory.append(potion)
                dining_hall_two.inventory.append(armor)
                player.key_used = True
                scene_four_sect_two(player)
            elif not player.key_used:
                print('\nYou do not have the key to the room')
                scene_four_sect_two(player)
            else:
                print('\nYou have already opened the room.')
                scene_four_sect_two(player)
        elif 'back' in answer:
            print('\nYou make your way back to the previous room')
            scene_four_sect_one(player)
        else:
            print('\nYou cannot do that.')
            time.sleep(2)
            scene_four_sect_two(player)


# ------------------------ Finale ----------------


def finale_sect_one(player):
    """
    Finale, main hall foyer, large room with 3 sections
    """
    player.current_room = main_hall_one
    if mother_ogre in main_hall_one.inventory:
        print('\nAn absolutely gigantic Ogre stands tall in the middle'
              ' of the room. It seems it heard you murder its child. Woops.')
    else:
        pass
    combat(player, mother_ogre, finale_sect_one)
    print('\n[Main Hall Foyer] What do you do?')
    answer = ''
    while answer == '':
        answer = input('\n').lower()
        check_generics(player, answer, main_hall_one, finale_sect_one)
        if 'stairs' in answer or 'up' in answer:
            print('You begin climbing the gigantic stairs and reach'
                  ' a midway point. A bonfire, lit, sits in the middle.'
                  ' The bonfire fully heals you as you sit down.')
            player.health = player.max_health
            finale_sect_two(player)
        elif 'back' in answer:
            print('\nYou make your way back to the previous room')
            scene_four_sect_two(player)
        else:
            print('\nYou cannot do that.')
            time.sleep(2)
            finale_sect_one(player)


def finale_sect_two(player):
    """
    Finale, main hall stairs, large room with 3 sections
    """
    player.current_room = main_hall_two
    print('\n[Main Hall Stairs] What do you do?')
    answer = ''
    while answer == '':
        answer = input('\n').lower()
        check_generics(player, answer, main_hall_two, finale_sect_two)
        if 'stairs' in answer or 'up' in answer:
            print('You push on and up the rest of the stairs.'
                  ' Your heart beats faster and louder as you know you'
                  ' are nearing the end. You reach the throne room.')
            finale_sect_three(player)
        elif 'sword' in answer or 'pull' in answer:
            if player.good_person:
                print('\nThe Sword deems you worthy and releases from the'
                      ' bonfire.'
                      ' Excalibur, the Legendary Sword, is now yours.')
                player.update_inventory(excalibur)
                finale_sect_two_v2(player)
            else:
                print('\nThe Sword deems you unworthy and is immovable')
        elif 'back' in answer:
            print('\nYou make your way back to the previous room')
            finale_sect_one(player)
        else:
            print('\nYou cannot do that.')
            time.sleep(2)
            finale_sect_two(player)


def finale_sect_two_v2(player):
    """
    Finale, main hall stairs with no excalibur, large room with 3 sections
    """
    player.current_room = main_hall_two_v2
    print('\n[Main Hall Stairs] What do you do?')
    answer = ''
    while answer == '':
        answer = input('\n').lower()
        check_generics(player, answer, main_hall_two, finale_sect_two)
        if 'stairs' in answer or 'up' in answer:
            print('You push on and up the rest of the stairs.'
                  ' Your heart beats faster and louder as you know you'
                  ' are nearing the end. You reach the throne room.')
            finale_sect_three(player)
        elif 'back' in answer:
            print('\nYou make your way back to the previous room')
            finale_sect_one(player)
        else:
            print('\nYou cannot do that.')
            time.sleep(2)
            finale_sect_two_v2(player)


def finale_sect_three(player):
    """
    Finale, main hall throne room, last boss and win condition
    """
    player.current_room = main_hall_three
    print('\nSomething is not right. The Rose sits out in the open in front'
          ' of the Throne, ripe for the taking.')
    time.sleep(2)
    print('\nJust as you suspected, a mysterious figure walks out from'
          ' behind one of the pillars, slowly clapping...')
    time.sleep(1)
    print(f'"\nWell done, {player.name}, I truly did not think you'
          ' would make it this far. However I,'
          ' Mergo, Guardian of the Rose cannot allow you to live.'
          'Goodbye."')
    time.sleep(2)
    combat(player, final_boss, finale_sect_three)
    print('\nCongratulations! You have attained the Legendary Rose,'
          ' and defeated the evil Mergo.'
          f' Be proud, {player.name}, and give that Rose to someone worthy.')
    quit()


# --------------------------------------- Main Game --------------------------


def main():
    """
    Main game function
    """
    menu()
    os.system('clear')
    player = Player(input('\nWhat is your name, Hero?\n'), 100, 100, [],
                    hands, True, cellar, True, False, False)
    print(f'\nAh, {player.name}, a fine name for a budding adventurer.')
    print(f'\nAre you a good person, {player.name}? Y/N')
    good = ''
    while good == '':
        good = input('\n').lower()
        if 'n' in good:
            player.good_person = False
        else:
            pass
    time.sleep(2)
    print("""\nYou find yourself in a dimly lit cellar.
You have been told this cellar leads to a secret passage
directly to the Throne Room of Castle Rose.
Ahead of you lies a single door... but perhaps you should
look around first?""")
    time.sleep(2)
    scene_one(player)


main()
