responses = {}

inquiry_active = True

while inquiry_active:
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")

    responses[name] = response

    repeat = input("Would you like to allow another person take the test? (Yes/No) ")
    if repeat.lower() == 'no':
        inquiry_active = False

print("\n--- Polling Results ---")
for name, response in responses.items():
    print(name + " would like to visit " + response + ".")
