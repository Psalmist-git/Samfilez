footballers = []

footballers.append('palmer'.title())
footballers.append('pedro'.title())
footballers.append('morgan'.title())

print(footballers)

footballers = ['palmer', 'pedro', 'morgan']
footballers.insert(3, 'caicedo')
print(footballers)

del footballers[3]
print(footballers)

footballers.insert(3, 'james')
print(footballers)

footballers = ['palmer', 'pedro', 'morgan']
print(footballers)

popped_footballers = footballers.pop(0)
print(footballers)
print(popped_footballers)

footballers = ['palmer', 'pedro', 'morgan']

best_player = footballers.pop(0)
print("The current best player at chelsea football club is " + best_player.title() + ".")

footballers = ['palmer', 'pedro', 'morgan']
best_player = footballers.pop(2)
print("The player with the most assist at chelsea football club is " + best_player.title())

footballers = ['palmer', 'pedro', 'morgan']
best_player = footballers.pop(1)
print("The player with the most goals at chelsea football club is " + best_player.title() + ".")

footballers = ['palmer', 'pedro', 'morgan']
best_duo = footballers.pop(1)
print("The best duo at CFC are " + best_duo.title() + ".")

footballers.insert(3, 'james')
print(footballers)
footballers.insert(4, 'colwill')
print(footballers)

footballers = ['palmer', 'pedro', 'morgan', 'james', 'colwill']
print(footballers)

footballers.remove('colwill')
print(footballers)

del footballers[3]
print(footballers)

footballers.insert(3, 'james')
print(footballers)

footballers = ['palmer', 'pedro', 'morgan', 'james', 'colwill']
print(footballers)

footballers = ['palmer', 'pedro', 'morgan', 'james', 'colwill']
print(footballers)

footballers = 'morgan'
print(footballers)
print("\n " + footballers.title() + " is the most expendable player at CFC for me.")