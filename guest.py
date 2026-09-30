filename = 'guest_list.txt'

with open(filename, 'w') as file_object:
    # Combined into 1 single string argument
    file_object.write('Nina, cheke, law, fred') 

with open(filename) as file_object:
    lines = file_object.readlines()

guest_string = ''
for line in lines:
    guest_string += line.rstrip()

guest = input("What is your name? ")
if guest in guest_string:
    print("Welcome " + guest.title() + "," + " to this program.\n")
    print("Welcome to my induction ceremony\n")
else:
    print("Sorry, but you are not allowed in here\n")
    print("Goodbye and have a great day.")