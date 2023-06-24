class Items:

    class Potion:

        def __init__(self, name, description):
            self.item_class = 'Potion'
            self.name = name
            self.description = description
            if self.description[0] == 'Heal':
                self.heal_amount = int(self.description[1:])

    class Weapon:

        def __init__(self, name, description):
            self.item_class = 'Weapon'
            self.name = name
            self.description = description

    class Armor:

        def __init__(self, name, amount):
            self.item_class = 'Armor'
            self.name = name
            self.amount = amount