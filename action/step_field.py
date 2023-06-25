from random import randint, choice
from time import sleep


def battle(creatures: dict, name_agility) -> bool:

    def turn(npc=True):
        SLEEP_TIME = 0.5

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
            sleep(SLEEP_TIME)

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
                sleep(SLEEP_TIME)

            # TODO: create logic for healing creatures in one team (enemy or allies)

            if dice_2 == 'heal':
                print(f'{creatures.get(name).name} heals for {heal}\n')
                if creatures.get(name).current_hp + heal >= creatures.get(name).max_hp:
                    creatures.get(name).current_hp = creatures.get(name).max_hp
                else:
                    creatures.get(name).current_hp += heal
                sleep(SLEEP_TIME)
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
                      f'also you can run away from battlefield (just enter RUN!): ')
            if s == 'attack':
                if creatures.get(name).enemy:  # is True
                    r = input(('Enter name of enemy: ' + '{}, ' * len(allies) + '\nEnter: ').format(*allies))
                    creatures.get(r).current_hp -= attack
                else:  # is False
                    r = input(('Enter name of enemy: ' + '{}, ' * len(enemy) + '\nEnter: ').format(*enemy))
                    creatures.get(r).current_hp -= attack
                print(f'{creatures.get(r).name} attacked by {creatures.get(name).name} for {attack} damage')
                sleep(SLEEP_TIME)

            elif s == 'heal':
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
            elif s == 'RUN':
                print(f'{name} runs away from battlefield\n')
                if creatures.get(name).enemy:
                    enemy.remove(name)
                else:
                    allies.remove(name)
                name_agility.remove(name)
                sleep(SLEEP_TIME)

    name_agility = list(dict(sorted(name_agility.items(), key=lambda x: x[1])))[::-1]
    print(('Turn order: ' + '{}, ' * len(name_agility)).format(*name_agility))
    sleep(1)
    enemy = []
    allies = []

    for creature in creatures:
        if creatures.get(creature).enemy is True:
            enemy.append(creature)
        elif creatures.get(creature).enemy is False:
            allies.append(creature)

    while len(enemy) > 0 or len(allies) > 0:
        for name in name_agility:
            if len(allies) == 0:
                print("There are no more allies\n")
                return False
            if len(enemy) == 0:
                print("There are no more enemies\n")
                return True

            amount_of_turns = creatures.get(name).agility // 10
            if amount_of_turns == 0:
                amount_of_turns = 2

            if creatures.get(name).npc:
                for _ in range(amount_of_turns):
                    if creatures.get(name).name in name_agility:
                        turn()
                    else:
                        break
            else:
                for _ in range(amount_of_turns):
                    if creatures.get(name).name in name_agility:
                        turn(npc=False)
                    else:
                        break
            if creatures.get(name).current_hp <= 0:
                if name in allies:
                    print(creatures.get(name).name + ' is died\n')
                    allies.remove(name)
                    name_agility.remove(name)
                elif name in enemy:
                    print(creatures.get(name).name + ' is died\n')
                    enemy.remove(name)
                    name_agility.remove(name)

            print('Enemy:')
            for i in enemy:
                print(f'{creatures.get(i).name}: {creatures.get(i).current_hp}/{creatures.get(i).max_hp}')
            print('Allies:')
            for i in allies:
                print(f'{creatures.get(i).name}: {creatures.get(i).current_hp}/{creatures.get(i).max_hp}')
            print()
