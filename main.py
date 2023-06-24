from models.creatures import Creatures
import action.step_field as sf
import json


def main():
    def call_info():
        name = input(f'Name of creature: ')
        try:
            print('-==-==-==-')
            print(f'Type: {dict_of_creatures.get(f"{name}").type}\n',
                  f'Name: {dict_of_creatures.get(f"{name}").name}\n',
                  f'Strength: {dict_of_creatures.get(f"{name}").strength}\n',
                  f'Agility: {dict_of_creatures.get(f"{name}").agility}\n',
                  f'Intelligence: {dict_of_creatures.get(f"{name}").intelligence}\n',
                  f'Wisdom: {dict_of_creatures.get(f"{name}").wisdom}\n',
                  f'Shield: {dict_of_creatures.get(f"{name}").shield}\n',
                  f'Max hp: {dict_of_creatures.get(f"{name}").max_hp}\n',
                  f'Current hp: {dict_of_creatures.get(f"{name}").current_hp}\n',
                  f'Armor: {dict_of_creatures.get(f"{name}").armor}\n',
                  f'Spells: {dict_of_creatures.get(f"{name}").spells}\n',
                  f'Inventory: {dict_of_creatures.get(f"{name}").inventory}\n',
                  f'NPC: {dict_of_creatures.get(f"{name}").npc}\n',
                  f'God: {dict_of_creatures.get(f"{name}").god}\n',
                  f'Enemy: {dict_of_creatures.get(f"{name}").enemy}\n',
                  f'Dead: {dict_of_creatures.get(f"{name}").dead}\n',
                  )
            print('-==-==-==-')
        except NameError:
            print('Name not found')

    def add_creature():
        s = input('Add alive or undead?\n')
        match s:
            case 'alive':
                name = input(f'Enter name of alive creature:\n')
                dict_of_creatures[f'{name}'] = Creatures.Alive(name)

            case 'undead':
                name = input(f'Enter name of undead creature:\n')
                dict_of_creatures[f'{name}'] = Creatures.Undead(name)
            case _:
                print('Invalid input')

    # TODO: add functionality to main function. Add item to inventory - also add to main function
    def add_spell(nm: str):
        dict_of_creatures.get(f'{nm}').spells.append(input(f'Enter spell name:\n'))

    def edit_creature(nm: str, st: str, xv=None):
        match st:
            case 'name':
                name = input('Enter a new name: ')
                dict_of_creatures[f'{name}'] = dict_of_creatures.get(f'{nm}')
                dict_of_creatures[f'{name}'].name = name
                del dict_of_creatures[f'{nm}']
            case 'level':
                dict_of_creatures[f'{nm}'].level = xv
            case 'strength':
                dict_of_creatures[f'{nm}'].strength = xv
                dict_of_creatures[f'{nm}'].max_hp = dict_of_creatures[f'{nm}'].calc_max_hp()
            case 'agility':
                dict_of_creatures[f'{nm}'].agility = xv
            case 'intelligence':
                dict_of_creatures[f'{nm}'].intelligence = xv
            case 'wisdom':
                dict_of_creatures[f'{nm}'].wisdom = xv
            case 'shield':
                dict_of_creatures[f'{nm}'].shield = xv
            case 'current_hp':
                dict_of_creatures[f'{nm}'].current_hp = xv
            case 'armor':
                dict_of_creatures[f'{nm}'].armor = xv
            case 'spells':
                dict_of_creatures[f'{nm}'].spells = xv
            case 'inventory':
                dict_of_creatures[f'{nm}'].inventory = xv
            case 'npc':
                dict_of_creatures[f'{nm}'].npc = xv
            case 'god':
                dict_of_creatures[f'{nm}'].god = xv
            case 'enemy':
                dict_of_creatures[f'{nm}'].enemy = xv
            case 'dead':
                dict_of_creatures[f'{nm}'].dead = xv
            case _:
                print('Invalid input')

    def load_creatures():
        s = input('Enter file name (wout .json)\n'
                  'Enter: ')
        with open(f'saves/{s}.json', 'r') as js:
            d = json.load(js)
            for i in range(len(d)):
                try:
                    if d[i]['type'] == 'Alive':
                        dict_of_creatures[d[i]['name']] = Creatures.Alive(name=d[i]['name'],
                                                                          level=d[i]['level'],
                                                                          strength=d[i]['strength'],
                                                                          agility=d[i]['agility'],
                                                                          intelligence=d[i]['intelligence'],
                                                                          wisdom=d[i]['wisdom'],
                                                                          shield=d[i]['shield'],
                                                                          current_hp=d[i]['current_hp'],
                                                                          armor=d[i]['armor'],
                                                                          spells=d[i]['spells'],
                                                                          inventory=d[i]['inventory'],
                                                                          npc=d[i]['npc'],
                                                                          god=d[i]['god'],
                                                                          enemy=d[i]['enemy'],
                                                                          dead=d[i]['dead'])
                    elif d[i]['type'] == 'Undead':
                        dict_of_creatures[f'{d[i]["name"]}'] = Creatures.Undead(d[i]['name'])
                except FileNotFoundError:
                    print('Error in load file or wrong file name')

    def save_creatures():
        s = input('Save all creatures or only one (enter "all" or name of creature)?\n'
                  'Enter: ')
        match s:
            case 'all':
                lst = []
                for i in dict_of_creatures:
                    d = {'type': dict_of_creatures.get(i).type,
                         'name': dict_of_creatures.get(i).name,
                         'level': dict_of_creatures.get(i).level,
                         'strength': dict_of_creatures.get(i).strength,
                         'agility': dict_of_creatures.get(i).agility,
                         'intelligence': dict_of_creatures.get(i).intelligence,
                         'wisdom': dict_of_creatures.get(i).wisdom,
                         'shield': dict_of_creatures.get(i).shield,
                         'current_hp': dict_of_creatures.get(i).current_hp,
                         'armor': dict_of_creatures.get(i).armor,
                         'spells': dict_of_creatures.get(i).spells,
                         'inventory': dict_of_creatures.get(i).inventory,
                         'npc': dict_of_creatures.get(i).npc,
                         'god': dict_of_creatures.get(i).god,
                         'enemy': dict_of_creatures.get(i).enemy,
                         'dead': dict_of_creatures.get(i).dead}
                    lst.append(d)
                with open('saves/all_creatures.json', 'w') as js:
                    json.dump(lst, js, indent=3)
            case _ if s in dict_of_creatures:
                if dict_of_creatures[f'{s}'].type == 'Alive':
                    d = [{'type': dict_of_creatures.get(f'{s}').type,
                          'name': dict_of_creatures.get(f'{s}').name,
                          'level': dict_of_creatures.get(f'{s}').level,
                          'strength': dict_of_creatures.get(f'{s}').strength,
                          'agility': dict_of_creatures.get(f'{s}').agility,
                          'intelligence': dict_of_creatures.get(f'{s}').intelligence,
                          'wisdom': dict_of_creatures.get(f'{s}').wisdom,
                          'shield': dict_of_creatures.get(f'{s}').shield,
                          'current_hp': dict_of_creatures.get(f'{s}').current_hp,
                          'armor': dict_of_creatures.get(f'{s}').armor,
                          'spells': dict_of_creatures.get(f'{s}').spells,
                          'inventory': dict_of_creatures.get(f'{s}').inventory,
                          'npc': dict_of_creatures.get(f'{s}').npc,
                          'god': dict_of_creatures.get(f'{s}').god,
                          'enemy': dict_of_creatures.get(f'{s}').enemy,
                          'dead': dict_of_creatures.get(f'{s}').dead}]
                    with open(f'saves/{s}.json', 'w') as js:
                        json.dump(d, js, indent=3)
                elif dict_of_creatures[f'{s}'].type == 'Undead':
                    pass
            case _:
                print('Invalid input')

    dict_of_creatures = {}
    while True:

        s = input(f'Call info --- info\n'
                  f'Add creature --- add\n'
                  f'Edit creature --- edit\n'
                  f'Save creatures --- save\n'
                  f'Load creatures --- load\n'
                  f'Add spell --- add spell\n'
                  f'Add item to inventory --- add item\n'
                  f'Start battle --- start\n'
                  f'Close --- exit\n'
                  f'Enter: ').lower()

        match s:
            case 'info':
                call_info()
            case 'add':
                add_creature()
            case 'edit':
                n = input('Enter a name of creature: ')
                s = input('What do you want to edit: name, level, strength, agility,\n'
                          'intelligence, wisdom, shield, armor,\n'
                          'spells, inventory, npc, god, enemy, dead?\n'
                          'Enter: ').lower()
                if s in ('name',):
                    edit_creature(n, s)
                elif s in ('level', 'strength', 'agility', 'intelligence', 'wisdom', 'shield', 'current_hp', 'armor'):
                    x = int(input(f'New value of {s}: '))
                    edit_creature(n, s, x)
                elif s in ('spells', 'inventory'):
                    x = list(input(f'New value of {s} (e.g.: "knife, potion, etc"): '))
                    edit_creature(n, s, x)
                elif s in ('npc', 'god', 'enemy', 'dead'):
                    x = bool(input(f'New value of {s} (True/False): '))
                    edit_creature(n, s, x)
            case 'load':
                load_creatures()
            case 'save':
                save_creatures()
            case 'start':
                name_agility = {}
                creatures_for_battle = {}
                live_creatures = [name for name in dict_of_creatures if dict_of_creatures.get(name).dead is False]
                for name in live_creatures:
                    name_agility[f'{name}'] = dict_of_creatures.get(name).agility
                    creatures_for_battle[f'{name}'] = dict_of_creatures.get(name)
                res = sf.battle(creatures=creatures_for_battle, name_agility=name_agility)
                if res:
                    print('You win!')
                else:
                    print('You lose!')
            case 'exit':
                break
            case _:
                print('Invalid input')


if __name__ == '__main__':
    main()
