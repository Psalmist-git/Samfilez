sandwich_orders = ['banana', 'flakes', 'jelly']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)

    print("I made your " + current_sandwich + ".")

    finished_sandwiches.append(current_sandwich)

print("\n--- All Sandwiches Made for our esteemed clients ---")
for sandwich in finished_sandwiches:
    print(sandwich.title() + " sandwich")


sandwich_orders = ['banana', 'flakes', 'jelly', 'flakes', 'buns', 'flakes']
finished_sandwiches = []

print("\nSorry, we have completely run out of flakes today!")

while 'flakes' in sandwich_orders:
    sandwich_orders.remove('flakes')

while sandwich_orders:
    current_sandwichs = sandwich_orders.pop()

    print("I made your " + current_sandwichs + "sandwich.")
    finished_sandwiches.append(current_sandwichs)

print("\n--- Finito ---")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()} sandwich")
