from models.creatures import Creatures


def main():
    dict_of_creatures = {}
    while True:
        s = input(f'Call info --- info\n'
                  f'Add creature --- add\n'
                  f'Close --- exit\n'
                  f'Input: ').lower()

        match s:

            case 'info':
                name = input(f'Name of creature:\n')
                try:
                    print(f' Name: {dict_of_creatures.get(f"{name}").name}\n',
                          f'Strength: {dict_of_creatures.get(f"{name}").strength}\n',
                          f'Agility: {dict_of_creatures.get(f"{name}").agility}\n',
                          f'Intelligence: {dict_of_creatures.get(f"{name}").intelligence}\n',
                          f'Wisdom: {dict_of_creatures.get(f"{name}").wisdom}\n')
                except:
                    print('Error')

            case 'add':
                s = input('Add alive or undead?\n')
                match s:
                    case 'alive':
                        name = input(f'Input name of alive creature:\n')
                        dict_of_creatures[f'{name}'] = Creatures.Alive(name)

                    case 'undead':
                        name = input(f'Input name of undead creature:\n')
                        dict_of_creatures[f'{name}'] = Creatures.Undead(name)


            case 'exit':
                break


if __name__ == '__main__':
    main()
