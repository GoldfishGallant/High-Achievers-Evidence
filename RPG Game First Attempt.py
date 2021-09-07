#Objects
class char:
    def __init__(self, name, char_race, char_class, char_stats):
        self.name = name
        self.char_race = char_race
        self.char_class = char_class
        self.char_stats = char_stats
        
    def __str__(self):
        return(f'''
-------{self.name}-------
Race: {self.char_race}
Class: {self.char_class}

--Stats--
Attack: {self.char_stats['Atk']}
Defence: {self.char_stats['Def']}
Agility: {self.char_stats['Agi']}
Wisdom: {self.char_stats['Wis']}
''')

class enemy:
    def __init__(self, enemy_name, enemy_race, enemy_stats, loot_table):
        self.enemy_name = enemy_name
        self.enemy_race = enemy_race
        self.enemy_stats = enemy_stats
        self.loot_table = loot_table
        

    def __str__(self):
        return(f'''
-------{self.enemy_name}-------
Race: {self.enemy_race}

--Stats--
Attack: {self.enemy_stats['Atk']}
Defence: {self.enemy_stats['Def']}
Agility: {self.enemy_stats['Agi']}
Wisdom: {self.enemy_stats['Wis']}

--Loot--
Weapons: {', '.join(self.loot_table['Weapons'])}
Armor: {self.loot_table['Armor']}
Potions: {self.loot_table['Potions']}
''')

class item:
    def __init__(self, item_name, values):
        self.item_name = item_name
        self.values = values
    def __str__(self):
        return (self.item_name)

#Functions

def char_create():
    name = input('What is your name? ')
    while True:
        try:
            char_race = int(input('''
---Please select a race---
1. Human
2. Orc
3. Zombie
'''))
            if char_race > 3 or char_race <= 0:
                raise ValueError('Invalid Number!')
            break
        
        except ValueError:
            print('Invalid number!')
            
    while True:
        try:   
            char_class = int(input('''
---Please select a class---
1. Warrior
2. Hunter
3. Mage
'''))
            if char_class > 3 or char_class <= 0:
                raise ValueError('Invalid Number!')
            break
        
        except ValueError:
            print('Invalid number!')
            
    races = {1:'Human',2:'Orc',3:'Zombie'}
    classes = {1:'Warrior',2:'Hunter',3:'Mage'}
    
    for race in races:
        if char_race == race:
            char_race = races[race]
    for _class in classes:
        if char_class == _class:
            char_class = classes[_class]

    char_stats = {'Atk': 8,'Def': 8,'Agi': 8,'Wis': 8}
    
    race_proficiencies = {'Human': {'Atk':1,'Def': 2,'Agi': 4,'Wis': 2},
                          'Orc': {'Atk': 4,'Def': 4,'Agi': 1,'Wis': -1},
                          'Zombie': {'Atk': 2,'Def': 0,'Agi': 3,'Wis': 4}}

    class_proficiencies = {'Warrior': {'Atk':4,'Def': 3,'Agi': 0,'Wis': 0},
                          'Hunter': {'Atk': 3,'Def': 2,'Agi': 3,'Wis': 0},
                          'Mage': {'Atk': 0,'Def': 1,'Agi': 1,'Wis': 5}}
    
    for stat_id, stat_info in char_stats.items():
        for race_prof_id, race_prof_info in race_proficiencies.items():
            if race_prof_id == char_race:
                for r_key in race_prof_info:
                    if r_key == stat_id:
                        char_stats[stat_id]=(stat_info+race_prof_info[r_key])
                        
    for stat_id, stat_info in char_stats.items():
        for class_prof_id, class_prof_info in class_proficiencies.items():
            if class_prof_id == char_class:
                for c_key in race_prof_info:
                    if c_key == stat_id:
                        char_stats[stat_id]=(stat_info+class_prof_info[c_key])



    return char(name, char_race, char_class, char_stats)
    

#Object Assignments
Club = item('Large Club', 3)
Stick = item('Stick', 2)
troll_stats = {'Atk': 8,'Def': 8,'Agi': 8,'Wis': 8}
troll_loot_table = {'Weapons': (Club.__str__(), Stick.__str__()),
                    'Armor': 'Torn Cloth',
                    'Potions': ''}
enemy1 = enemy('Common Troll', 'Troll', troll_stats, troll_loot_table)



char1 = char_create()
print(char1)
print(enemy1)

