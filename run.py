# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

inventory = ['ladybug', 'test vial', 'garbage bag']

class Human(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health


bandit = Human('Bandit', 100)


print('You attack the bandit!')
bandit.health -= 50
print(f'The Bandits health is now {bandit.health}')


def good_or_bad():
    answer = ''
    while answer != 'yes' and answer != 'no':
        answer = input(f'A simple choice to start with {hero_name}, are you good and true of heart?\nYes/No: ').lower()
        alignment = ''
        if answer == 'yes':
            alignment = 'a stoic Knight, good and true of heart'
        else:
            alignment = 'a dark soul, ruthless and out for blood'
    return alignment


def scene_one():
    print("""
    What do you do?
    (E.g. Look around/Open Door/Inventory)
    """)
    answer = ''
    while (answer == ''):
        answer = input('').lower()
        if answer == 'look around' and 'torch' not in inventory:
            print('You see an unlit torch lying on the ground.')
            scene_one()
        elif answer == 'look around' and 'torch' in inventory:
            print('You see the soot from where the torch used to be.')
            scene_one()
        elif answer == 'inventory':
            print('The items in your inventory:')
            for item in inventory:
                print(f'- {item}')
            scene_one()
        elif answer == 'open door':
            print('Next Scene')
            break
        elif answer == 'stay here':
            print('You have died. Restart.')
            break
        elif 'torch' in answer and 'torch' not in inventory:
            print('You pick up the torch.')
            inventory.append('torch')
            scene_one()
        elif answer == 'quit':
            print('The Rose awaits your next attempt.')
            break
        else:
            print('You cannot do that.')
            scene_one()



# print("""
# Welcome Hero to The Legend of Rose.
# Your goal is to obtain the legendary Rose held in Castle Rosebush.
# Revered for it's incredible ability to flatter the one you love, 
# it is well guarded.
# You will face many challenges along the way, and the choices you make may 
# affect the outcome.\n""")

# hero_name = input('Please enter your characters name: ')

# print(f'\nAh, {hero_name}, a fine name for a valiant Knight.\n')

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