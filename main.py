from models.creatures import Creatures
# from models.items import Items
from models.spells import Spell
import action.step_field as sf
import json


def main():
    def call_info():
        name = input(f'Name of creature: ')
        try:
            print('-==-==-==-')
            print(f'Info of {name}')
            d = dict_of_creatures.get(name).__dict__
            for k in d:
                print(f'{k}: {d[k]}')
            print('-==-==-==-')
        except AttributeError:
            print('Name not found')

    def add_creature():
        s = input('Add alive or undead?\n')
        match s:
            case 'alive':
                name = input(f'Enter name of alive creature:\n')
                dict_of_creatures[name] = Creatures.Alive(name)

            case 'undead':
                name = input(f'Enter name of undead creature:\n')
                dict_of_creatures[name] = Creatures.Undead(name)
            case _:
                print('Invalid input')

    # TODO: Add item to inventory - also add to main function

    def edit_creature(nm: str, st: str, xv=None):
        match st:
            case 'name':
                try:
                    name = input('Enter a new name: ')
                    dict_of_creatures[name] = dict_of_creatures.get(nm)
                    dict_of_creatures[name].name = name
                    del dict_of_creatures[nm]
                except AttributeError:
                    print('Name not found')
            case 'level':
                dict_of_creatures[nm].level = xv
            case 'strength':
                dict_of_creatures[nm].strength = xv
                dict_of_creatures[nm].max_hp = dict_of_creatures[nm].calc_max_hp()
            case 'agility':
                dict_of_creatures[nm].agility = xv
            case 'intelligence':
                dict_of_creatures[nm].intelligence = xv
            case 'wisdom':
                dict_of_creatures[nm].wisdom = xv
            case 'shield':
                dict_of_creatures[nm].shield = xv
            case 'current_hp':
                dict_of_creatures[nm].current_hp = xv
            case 'armor':
                dict_of_creatures[nm].armor = xv
            case 'spells':
                dict_of_creatures[nm].spells = xv
            case 'inventory':
                dict_of_creatures[nm].inventory = xv
            case 'npc':
                dict_of_creatures[nm].npc = xv
            case 'god':
                dict_of_creatures[nm].god = xv
            case 'enemy':
                dict_of_creatures[nm].enemy = xv
            case 'dead':
                dict_of_creatures[nm].dead = xv
            case _:
                print('Invalid input')

    def load_creatures():
        s = input('Enter file name (wout .json)\n'
                  'Enter: ')
        with open(f'saves/creatures/{s}.json', 'r') as js:
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
            if s == 'all_creatures':
                load_spells(s='all_spells')
            else:
                for j in d[0]['spells']:
                    load_spells(s=j)

    def save_creatures():
        s = input('Save all creatures or only one (enter "all" or name of creature)?\n'
                  'Enter: ')
        match s:
            case 'all':
                lst = []
                for i in dict_of_creatures:
                    d = dict_of_creatures.get(i).save()
                    lst.append(d)
                with open('saves/creatures/all_creatures.json', 'w') as js:
                    json.dump(lst, js, indent=3)
                save_spells(s='all')
            case _ if s in dict_of_creatures:
                if dict_of_creatures[s].type == 'Alive':
                    d = [dict_of_creatures.get(s).save()]

                    with open(f'saves/creatures/{s}.json', 'w') as js:
                        json.dump(d, js, indent=3)
                    for i in dict_of_creatures.get(s).spells:
                        save_spells(s=i)
                elif dict_of_creatures[s].type == 'Undead':
                    pass
            case _:
                print('Invalid input')

    def add_spell(name: str, desc: str, heal_amount: int, damage_amount: int, type_spell: str):
        dict_of_spells[name] = Spell(name, desc, heal_amount, damage_amount, type_spell)

    def info_spell(name: str):
        try:
            print('-==-==-==-')
            print(f'Info of {name}')
            d = dict_of_spells.get(name).__dict__
            for k in d:
                print(f'{k}: {d[k]}')
            print('-==-==-==-')
        except AttributeError:
            print('Name of spell not found')

    def save_spells(s):
        match s:
            case 'all':
                lst = []
                for i in dict_of_spells:
                    d = dict_of_spells.get(i).save()
                    lst.append(d)
                with open('saves/spells/all_spells.json', 'w') as js:
                    json.dump(lst, js, indent=3)
            case _ if s in dict_of_spells:
                d = [dict_of_spells.get(s).save()]
                with open(f'saves/spells/{s}.json', 'w') as js:
                    json.dump(d, js, indent=3)
            case _:
                print('Invalid input')

    def add_spell_to_creature(name_creature: str, spell: str):
        if name_creature in dict_of_creatures or spell in dict_of_spells:
            if not dict_of_creatures[name_creature].spells:
                dict_of_creatures[name_creature].spells = [spell, ]
            else:
                sp = list(*[dict_of_creatures[name_creature].spells])
                sp.append(spell)
                dict_of_creatures[name_creature].spells = sp
        else:
            print('Creature or spell not found')

    def load_spells(s):
        with open(f'saves/spells/{s}.json', 'r') as js:
            d = json.load(js)
            for i in range(len(d)):
                try:
                    dict_of_spells[d[i]['name']] = Spell(name=d[i]['name'],
                                                         description=d[i]['description'],
                                                         heal_amount=d[i]['heal_amount'],
                                                         damage_amount=d[i]['damage_amount'],
                                                         type_spell=d[i]['type_spell'],
                                                         )
                except FileNotFoundError:
                    print('Error in load file or wrong file name')

    dict_of_creatures = {}
    dict_of_spells = {}

    while True:

        s = input(f'Info about creature --- info\n'
                  f'Add creature --- add\n'
                  f'Edit creature --- edit\n'
                  f'Save creatures --- save\n'
                  f'Load creatures --- load\n'
                  f'Add spell --- spell\n'
                  f'Add spell to creature --- add spell\n'
                  f'Info about spell --- info spell\n'
                  f'Save spells --- save spells\n'
                  f'Load spells --- load spells\n'
                  f'Add item --- item\n'
                  f'Add item to creature --- add item\n'
                  f'Save items --- save items\n'
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
            case 'spell':
                name = input(f'Enter name of spell: ')
                desc = input(f'Enter description of spell: ')
                heal_amount = int(input(f'Enter heal amount: '))
                damage_amount = int(input(f'Enter damage amount: '))
                type_spell = input(f'Fire, water, ice, wind, earth or electro: ')
                add_spell(name, desc, heal_amount, damage_amount, type_spell)
                s = input(f'Do you want to add spell to creature? (Enter name of creature): ')
                if s in dict_of_creatures:
                    add_spell_to_creature(s, name)
                    print(f'Spell {name} added to creature {s}')
            case 'info spell':
                name = input(f'Name of spell: ')
                info_spell(name)
            case 'save spells':
                s = input('Save all spells or only one (enter "all" or name of spell)?\n'
                          'Enter: ')
                save_spells(s)
            case 'load spells':
                s = input('Enter file name (wout .json)\n'
                          'Enter: ')
                load_spells(s)
            case 'add spell':
                nm = input(f'Enter name of creature: ')
                sp = input(f'Enter name of spell: ')
                add_spell_to_creature(nm, sp)
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
