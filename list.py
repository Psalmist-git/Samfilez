family = ['francis', 'samson', 'moses', 'patience', 'samuel', 'john']
print(family)

banks = ['zenith'.title(), 'phb'.title(), 'access'.title(), 'opay'.title()]
print(banks)

print(family[1])
print(banks[3])

print(family[1].title())
print(banks[3].title())

print(family[-1].title())
print(banks[-2].title())

message = "My favorite family member is " + family[0].title() + "."
print(message)
message = "My favorite and most used bank is " + banks[-1].title() + "."
print(message)

banks = ['zenith'.title(), 'phb'.title(), 'access'.title(), 'opay'.title()]
print(banks)

banks[1] = 'guarantee trust bank'.title()
print(banks)

message = "My favorite family member is " + family[4].title() + "."
print(message)
message = "My favorite and most used bank is " + banks[2].title() + "."
print(message)

banks.append('fidelity, jaiz bank, sunset bank'.title())
print(banks)

cars = []

cars.append('toyota'.title())
cars.append('mercedez benz'.title())
cars.append('BMW'.title())
cars.append('range rover'.title())

print(cars)

family = ['francis', 'samson', 'moses', 'patience', 'samuel', 'john']
family.insert(1, 'mummy')
print(family)

family = ['francis', 'samson', 'moses', 'patience', 'samuel', 'john']
del family[0]
print(family)

family = ['francis', 'samson', 'moses', 'patience', 'samuel', 'john']
print(family)

popped_family = family.pop()
print(family)
print(popped_family)

family = ['francis', 'samson', 'moses', 'patience', 'samuel', 'john']
first_born = family.pop(5)
print("The last of our house is " + first_born.title() + ".")
