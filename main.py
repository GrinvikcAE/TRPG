from models.creatures import Creatures
import json


def main():
    def call_info():
        name = input(f'Name of creature:\n')
        try:
            print(f' Name: {dict_of_creatures.get(f"{name}").name}\n',
                  f'Strength: {dict_of_creatures.get(f"{name}").strength}\n',
                  f'Agility: {dict_of_creatures.get(f"{name}").agility}\n',
                  f'Intelligence: {dict_of_creatures.get(f"{name}").intelligence}\n',
                  f'Wisdom: {dict_of_creatures.get(f"{name}").wisdom}\n')
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

    def edit_creature(n,s):
        match s:
            case 'name':
                name = input('Enter a new name: ')
                dict_of_creatures[f'{name}'] = dict_of_creatures.get(f'{n}')
                dict_of_creatures[f'{name}'].name = name
                del dict_of_creatures[f'{n}']
            case 'level':
                pass

    def load_creatures():
        s = input('Enter file name (wout .json)'
                  'Enter: ')
        with open(f'{s}.json', 'r') as js:
            d = json.load(js)
            for i in range(len(d)):
                if d[i]['type'] == 'Alive':
                    dict_of_creatures[f'{d[i]["name"]}'] = Creatures.Alive(d[i]['name'])

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
                edit_creature(n,s)
            case 'load':
                load_creatures()
            case 'save':
                save_creatures()
            case 'exit':
                break


if __name__ == '__main__':
    main()
