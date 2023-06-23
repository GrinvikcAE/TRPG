from models.creatures import Creatures
import json


def main():
    def call_info():
        name = input(f'Name of creature: ')
        try:
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
                  )
        except:
            print('Error')

    def add_creature():
        s = input('Add alive or undead?\n')
        match s:
            case 'alive':
                name = input(f'Enter name of alive creature:\n')
                dict_of_creatures[f'{name}'] = Creatures.Alive(name)

            case 'undead':
                name = input(f'Enter name of undead creature:\n')
                dict_of_creatures[f'{name}'] = Creatures.Undead(name)

    def edit_creature(nm: str, st: str, *xv: int | list):
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

    def load_creatures():
        s = input('Enter file name (wout .json)\n'
                  'Enter: ')
        with open(f'{s}.json', 'r') as js:
            d = json.load(js)
            print(d)
            for i in range(len(d)):
                try:
                    if d[i]['type'] == 'Alive':
                        print(d[i]['name'])
                        dict_of_creatures[d[i]['name']] = Creatures.Alive(d[i]['name'])
                        edit_creature(d[i]['name'], 'level', int(d[i]['level']))
                        edit_creature(d[i]['name'], 'strength', int(d[i]['strength']))
                        edit_creature(d[i]['name'], 'agility', int(d[i]['agility']))
                        edit_creature(d[i]['name'], 'intelligence', int(d[i]['intelligence']))
                        edit_creature(d[i]['name'], 'wisdom', int(d[i]['wisdom']))
                        edit_creature(d[i]['name'], 'shield', int(d[i]['shield']))
                        edit_creature(d[i]['name'], 'current_hp', int(d[i]['current_hp']))
                        edit_creature(d[i]['name'], 'armor', int(d[i]['armor']))
                        edit_creature(d[i]['name'], 'spells', list(d[i]['spells']))
                        edit_creature(d[i]['name'], 'inventory', list(d[i]['inventory']))
                        edit_creature(d[i]['name'], 'npc', bool(d[i]['npc']))
                        edit_creature(d[i]['name'], 'god', bool(d[i]['god']))
                    elif d[i]['type'] == 'Undead':
                        dict_of_creatures[f'{d[i]["name"]}'] = Creatures.Undead(d[i]['name'])
                except:
                    print('Error')

    def save_creatures():
        s = input('Save all creatures or only one (enter "all" or name of creature)?\n'
                  'Enter: ')
        match s:
            case 'all':
                pass
            case _:
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
                          'god': dict_of_creatures.get(f'{s}').god}]
                    with open(f'{s}.json', 'w') as js:
                        json.dump(d, js, indent=3)
                elif dict_of_creatures[f'{s}'].type == 'Undead':
                    pass

    dict_of_creatures = {}
    while True:

        s = input(f'Call info --- info\n'
                  f'Add creature --- add\n'
                  f'Edit creature --- edit\n'
                  f'Save creatures --- save\n'
                  f'Load creatures --- load\n'
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
                          'spells, inventory, npc, god?\n'
                          'Enter: ').lower()
                if s in ('name',):
                    edit_creature(n, s)
                elif s in ('level', 'strength', 'agility', 'intelligence', 'wisdom', 'shield', 'current_hp', 'armor'):
                    x = int(input(f'New value of {s}: '))
                    edit_creature(n, s, x)
                elif s in ('spells', 'inventory'):
                    x = list(input(f'New value of {s} (e.g.: "knife, potion, etc"): '))
                    edit_creature(n, s, x)
                elif s in ('npc', 'god'):
                    x = bool(input(f'New value of {s} (True/False): '))
                    edit_creature(n, s, x)
            case 'load':
                load_creatures()
            case 'save':
                save_creatures()
            case 'exit':
                break


if __name__ == '__main__':
    main()
