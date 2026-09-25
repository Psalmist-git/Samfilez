# 1. First, define the complete blueprint (The Class)
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # INDENTED: These actions now belong to the Dog blueprint
    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")


# 2. Go all the way to the left margin to use the blueprint
my_dog = Dog('willie', 6)


# 3. Print the results
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# This works perfectly now because the actions are inside the blueprint!
my_dog.sit()
my_dog.roll_over()