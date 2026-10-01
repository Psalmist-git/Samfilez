filename = 'pi_digits.txt'

with open(filename) as file_objective:
    lines = file_objective.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))


filename = 'pi_digits.txt'

with open(filename) as file_objective:
    lines = file_objective.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))



