import json

# Prompt the user for their favorite number
fav_number = input("What is your favorite number? ")

# Store the number in a JSON file
filename = 'favorite_number.json'
with open(filename, 'w') as file_object:
    json.dump(fav_number, file_object)

print("Thanks! I'll remember that number.")


import json

filename = 'favorite_number.json'

try:
    # Read the number back from the JSON file
    with open(filename, 'r') as file_object:
        fav_number = json.load(file_object)
    
    # Print the success message
    print(f"I know your favorite number! It’s {fav_number}.")

except FileNotFoundError:
    print("I couldn't find your favorite number. Please run the first program first!")




