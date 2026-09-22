def display_message():
    print("I am learning how to define a function by calling it as well as how to use arguments and parameters!")

display_message()

def favorite_book(hellish):
    print(f"One of my favorite books is {hellish.title()}!")

favorite_book('hellish')


def descibe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

descibe_pet('dog', 'bosco')
descibe_pet('cat', 'charlie')
