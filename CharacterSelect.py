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

print(f'''
Name: {name}
Race: {char_race}
Class: {char_class} ''')