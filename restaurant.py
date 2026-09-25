class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.name.title() + " is packed with local and international dish.")

    def open_restaurant(self):
        print(self.name.title() + " is open 24hrs a week.")

my_restaurant = Restaurant('psalm bellefu', 'local & international dishes')

print("My restaurants name is " + my_restaurant.name.title() + ".")
print("We have all kinds of meals both " + my_restaurant.cuisine_type.title() + ".")


my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()


class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Self Name: " + self.name.title())
        print("Cuisine Type: " + self.cuisine_type.title())
        print("-" * 30)

    def open_restaurant(self):
        print(self.name.title() + " is open 24hrs a week.")

Restaurant_one = Restaurant('psalm bellefu', 'local & international dishes')
Restaurant_two = Restaurant('mama put', 'local dishes')
Restaurant_three = Restaurant('swavy', 'ChipsnChops')

Restaurant_one.describe_restaurant()
Restaurant_two.describe_restaurant()
Restaurant_three.describe_restaurant()
