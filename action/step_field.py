from random import randint, choice
from time import sleep


def turn(creatures, allies, enemy, name, npc=True):
    def healing(name, heal):
        if creatures.get(name).current_hp + heal >= creatures.get(name).max_hp:
            creatures.get(name).current_hp = creatures.get(name).max_hp
        else:
            creatures.get(name).current_hp += heal

    if npc:
        dice_1 = randint(1, 6)
        heal = creatures.get(name).wisdom + dice_1
        attack = creatures.get(name).intelligence + dice_1
        dice_2 = choice(['heal', 'attack'])
        sleep(2)

        if creatures.get(name).current_hp == creatures.get(name).max_hp and dice_2 == 'heal':
            dice_2 = 'attack'

        if dice_2 == 'attack':
            if creatures.get(name).enemy:  # is True
                r = choice(allies)
                creatures.get(r).current_hp -= attack
            else:  # is False
                r = choice(enemy)
                creatures.get(r).current_hp -= attack
            print(f'{creatures.get(r).name} attacked by {creatures.get(name).name} for {attack} damage\n')
            sleep(2)

        # TODO: create logic for healing creatures in one team (enemy or allies)

        if dice_2 == 'heal':
            print(f'{creatures.get(name).name} heals for {heal}\n')
            if creatures.get(name).current_hp + heal >= creatures.get(name).max_hp:
                creatures.get(name).current_hp = creatures.get(name).max_hp
            else:
                creatures.get(name).current_hp += heal
            sleep(2)
    else:
        print(f'{name} is ready to turn!')
        s = input(f'Enter number (1-6) from dice or enter "dice" to roll dice: ')
        if s == 'dice':
            dice_1 = randint(1, 6)
            print(f'{name} rolls {dice_1}')
        else:
            dice_1 = int(s)

        heal = creatures.get(name).wisdom + dice_1
        attack = creatures.get(name).intelligence + dice_1

        s = input(f'Enter what do you want to do (attack or heal),'
                  f'also you can run away from battlefield (just enter RUN): ')
        if s == 'attack':
            if creatures.get(name).enemy:  # is True
                r = input(('Enter name of enemy: ' + '{}, ' * len(allies) + '\nEnter: ').format(*allies))
                creatures.get(r).current_hp -= attack
            else:  # is False
                r = input(('Enter name of enemy: ' + '{}, ' * len(enemy) + '\nEnter: ').format(*enemy))
                creatures.get(r).current_hp -= attack
            print(f'{creatures.get(r).name} attacked by {creatures.get(name).name} for {attack} damage')
            sleep(2)

        if s == 'heal':
            if creatures.get(name).enemy:
                r = input(('Enter name of allies: ' + '{}, ' * len(enemy) + '\nEnter: ').format(*enemy))
                if r == 'self':
                    r = name
                healing(r, heal)
                print(f'{creatures.get(r).name} heals for {heal} by {name}')
            else:
                r = input(('Enter name of allies: ' + '{}, ' * len(allies) + '\nEnter: ').format(*allies))
                if r == 'self':
                    r = name
                healing(r, heal)
                print(f'{creatures.get(r).name} heals for {heal} by {name}')
        if s == 'RUN':
            print(f'{name} runs away from battlefield\n')
            creatures.get(name).current_hp = 0
            sleep(2)


def battle(creatures: dict, name_agility) -> bool:
    name_agility = list(dict(sorted(name_agility.items(), key=lambda x: x[1])))[::-1]
    print(('Turn order: ' + '{}, ' * len(name_agility)).format(*name_agility))
    sleep(1)
    enemy = []
    allies = []
    for creature in creatures:
        if creatures.get(creature).enemy is True:
            enemy.append(creature)
        if creatures.get(creature).enemy is False:
            allies.append(creature)
    while len(enemy) > 0 or len(allies) > 0:
        for name in name_agility:
            if len(allies) == 0:
                print("There are no more allies\n")
                return False
            if len(enemy) == 0:
                print("There are no more enemies\n")
                return True
            if creatures.get(name).npc is True:
                turn(creatures, allies, enemy, name, npc=True)
            else:
                turn(creatures, allies, enemy, name, npc=False)
            if creatures.get(name).enemy is False and creatures.get(name).current_hp <= 0:
                print(creatures.get(name).name + ' is died\n')
                allies.remove(name)
                name_agility.remove(name)
            if creatures.get(name).enemy is True and creatures.get(name).current_hp <= 0:
                print(creatures.get(name).name + ' is died\n')
                enemy.remove(name)
                name_agility.remove(name)
            for i in enemy:
                print('Enemy:')
                print(f'{creatures.get(i).name}: {creatures.get(i).current_hp}/{creatures.get(i).max_hp}')
            for i in allies:
                print('Allies:')
                print(f'{creatures.get(i).name}: {creatures.get(i).current_hp}/{creatures.get(i).max_hp}\n')
