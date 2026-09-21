prompt = "\nPlease enter your age to find your ticket price: "
prompt += "\n(Enter 'quit' to exit) "

while True:
    user_input = input(prompt)
    
    if user_input.lower() == 'quit':
        break
        
    age = int(user_input)
    
    if age < 3:
        print("Your ticket is free!")
    elif age <= 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")

prompt = "\nEnter a pizza topping (or type 'quit' to stop): "
topping = ""

while topping.lower() != 'quit':
    topping = input(prompt)
    if topping.lower() != 'quit':
        print("\nI'll add " + topping.title() + " to your pizza!")


prompt = "\nEnter a pizza topping (or type 'quit' to stop): "
active = True

while active:
    topping = input(prompt)
    if topping.lower() == 'quit':
        active = False
    else:
        print("I'll add " + topping.title() + " to your pizza!")


while True:
    print("This loop runs forever! Press Ctrl+C to close it.")
