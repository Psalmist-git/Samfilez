filename = '/home/student/path/to/your/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

# Print the first 50 decimal places (plus "3." at the start)
print(f"{pi_string[:52]}...")
print(f"Total length of string: {len(pi_string)} characters.")
