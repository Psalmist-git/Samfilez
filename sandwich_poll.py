sandwich_orders = ['banana', 'flakes', 'jelly']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)

    print("I made your " + current_sandwich + ".")

    finished_sandwiches.append(current_sandwich)

print("\n--- All Sandwiches Made for our esteemed clients ---")
for sandwich in finished_sandwiches:
    print(sandwich.title() + " sandwich")