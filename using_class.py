class Dog():                                    # Defines the "Dog" blueprint (class) for creating dog objects
    def __init__(self, name, age):              # The initializer method that runs automatically when a new dog is made
        self.name = name                        # Stores the given name inside the dog object's "name" attribute
        self.age = age                          # Stores the given age inside the dog object's "age" attribute

    def sit(self):                              # Defines the "sit" action method for the dog
        print(self.name.title() + " is now sitting.")  # Capitalizes the name and prints that the dog is sitting

    def roll_over(self):                        # Defines the "roll_over" action method for the dog
        print(self.name.title() + " rolled over!")     # Capitalizes the name and prints that the dog rolled over


my_dog = Dog('willie', 6)                       # Creates an instance of Dog named 'willie' who is 6 years old

print("My dog's name is " + my_dog.name.title() + ".")  # Fetches, capitalizes, and prints the dog's name attribute
print("My dog is " + str(my_dog.age) + " years old.")  # Converts the age number to text and prints the dog's age

my_dog.sit()                                    # Calls the sit method to make Willie perform the sitting action
my_dog.roll_over()                              # Calls the roll_over method to make Willie roll over


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
    print("We have all kinds of meals at " + my_restaurant.cuisine_type.title() + ".")


my_restaurant.packed()
my_restaurant.everyday_a_week()