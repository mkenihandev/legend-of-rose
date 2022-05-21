# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

inventory = []
room_one = ['torch']


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
    print(room_one)
    print("""
    What do you do?
    (Look around/Open Door/Inventory)
    """)
    answer = ''
    while answer != 'look around' and answer != 'open door' and answer != 'inventory':
        answer = input('').lower()
        if answer == 'look around':
            print('You see an unlit torch lying on the ground. Take it?')
            torch_take = input('').lower()
            if torch_take == 'yes' and 'torch' in room_one:
                inventory.append('torch')
                scene_one()
                room_one.remove('torch')
            elif torch_take == 'yes' and 'torch' not in room_one:
                print('You already have that')
            elif torch_take == 'no':
                scene_one()
        elif answer == 'inventory':
            print(inventory)
            scene_one()
        elif answer == 'open door':
            print('onward')
        elif answer == 'stay here':
            print('You have died. Restart.')


print("""
Welcome Hero to The Legend of Rose.
Your goal is to obtain the legendary Rose held in Castle Rosebush.
Revered for it's incredible ability to flatter the one you love, 
it is well guarded.
You will face many challenges along the way, and the choices you make may 
affect the outcome.\n""")

hero_name = input('Please enter your characters name: ')

print(f'\nAh, {hero_name}, a fine name for a valiant Knight.\n')

alignment = good_or_bad()

print(f'\nYou are {alignment}, interesting.')

print("""
    You stand in a single square room of a sprawling dungeon. 
    You were told at the end of this dungeon, a secret passage can be found 
    leading directly to the throne room of Caslte Rosebush, 
    where the Rose is held.
    Ahead of you, there is a door.
    """)

scene_one()
print(room_one)