from random import randint, choice
from time import sleep
from models.creatures import Creatures


def move(creatures, allies, enemy, name):
    dice_1 = randint(1, 6)
    dice_2 = randint(1, 2)
    heal = creatures.get(name).wisdom + dice_1 #dice_2=2
    attack = creatures.get(name).intelligence + dice_1 #dice_2=1
    if creatures.get(name).current_hp == creatures.get(name).max_hp and dice_2 == 2:
        dice_2 = 1

    if dice_2 == 1:
        if creatures.get(name).enemy is True:
            r = choice(allies)
            creatures.get(r).current_hp -= attack
        else:
            r = choice(enemy)
            creatures.get(r).current_hp -= attack
        print(f'{creatures.get(r).name} attacked by {creatures.get(name).name} by {attack}')
        sleep(2)

    if dice_2 == 2:
        print(f'Heal {creatures.get(name).name} by {heal}')
        if creatures.get(name).current_hp + heal >= creatures.get(name).max_hp:
            creatures.get(name).current_hp = creatures.get(name).max_hp
        else:
            creatures.get(name).current_hp += heal
        sleep(2)


def battle(creatures: dict, name_agility) -> bool:
    name_agility = list(dict(sorted(name_agility.items(), key=lambda x: x[1])))
    print(('Turn order: ' + '{}, ' * len(name_agility)).format(*name_agility))
    sleep(2)
    enemy = []
    allies = []
    res = 0
    # while True:
    for creature in creatures:
        if creatures.get(creature).enemy is True:
            enemy.append(creature)
        if creatures.get(creature).enemy is False:
            allies.append(creature)
    while len(enemy) > 0 or len(allies) > 0:
        for name in name_agility:
            if len(allies) == 0:
                print("There are no more allies")
                return False
            if len(enemy) == 0:
                print("There are no more enemies")
                return True
            move(creatures, allies, enemy, name)
            if creatures.get(name).enemy is False and creatures.get(name).current_hp <= 0:
                print(creatures.get(name).name + ' is died')
                allies.remove(name)
                name_agility.remove(name)
            if creatures.get(name).enemy is True and creatures.get(name).current_hp <= 0:
                print(creatures.get(name).name + ' is died')
                enemy.remove(name)
                name_agility.remove(name)
            for i in name_agility:
                print(f'{creatures.get(i).name}: {creatures.get(i).current_hp}/{creatures.get(i).max_hp}')







