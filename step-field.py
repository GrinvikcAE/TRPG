from random import randint
from models.creatures import Creatures


def move(creatures, allies, enemy):

    pass


def battle(creatures: dict, name_agility):
    name_agility = list(dict(sorted(name_agility.items(), key=lambda x: x[1])))
    print(('Turn order: ' + '{}, ' * len(name_agility)).format(*name_agility))
    enemy = []
    allies = []
    flag = True
    while flag:
        for creature in creatures:
            if creatures.get(creature).enemy is True:
                enemy.append(creature)
            if creatures.get(creature).enemy is False:
                allies.append(creature)
        # for creature in creatures:
        #     if creatures.get(creature).enemy is False and creatures.get(creature).current_hp <= 0:
        #         print(creatures.get(creature).name + ' is died')
        #         allies.remove(creature)
        #     if creatures.get(creature).enemy is True and creatures.get(creature).current_hp <= 0:
        #         print(creatures.get(creature).name + ' is died')
        #         enemy.remove(creature)
        if len(allies) == 0:
            print("There are no more allies")
            flag = False    #TODO: add return statement
        if len(enemy) == 0:
            print("There are no more enemies")
            flag = False

        move(creatures, allies, enemy)

