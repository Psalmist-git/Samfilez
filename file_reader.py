with open('pi_digits.txt') as file_objective:
    contents = file_objective.read()
    print(contents)
    print(contents.rstrip())


filename = 'pi_digits.txt'

with open(filename) as file_objective:
    for line in file_objective:
        print(line)


filename = 'pi_digits.txt'

with open(filename) as file_objective:
    for line in file_objective:
        print(line.rstrip())


filename = 'pi_digits.txt'

with open(filename) as file_objective:
    lines = file_objective.readlines()

for line in lines:
    print(line.rstrip())