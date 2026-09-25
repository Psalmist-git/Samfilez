class Restaurant:
    """A class representing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name, cuisine type, and customers served."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Default value set to 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        print(f"{self.restaurant_name} serves delicious {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Display a message indicating the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        """Set the number of customers served to a specific value."""
        if number >= self.number_served:
            self.number_served = number
        else:
            print("You can't roll back the number of served customers!")

    def increment_number_served(self, additional_customers):
        """Add the given amount to the total number of customers served."""
        if additional_customers >= 0:
            self.number_served += additional_customers
        else:
            print("You can't add negative customers!")


# 1. Create an instance called restaurant
restaurant = Restaurant("The Gourmet Hub", "Italian")

# 2. Print initial number served, change it directly, and print again
print(f"Initial customers served: {restaurant.number_served}")
restaurant.number_served = 15
print(f"Updated directly to: {restaurant.number_served}")

# 3. Use set_number_served() method
restaurant.set_number_served(35)
print(f"Set via method to: {restaurant.number_served}")

# 4. Use increment_number_served() method
restaurant.increment_number_served(120)  # Representing a day of business
print(f"After a full day of business, total served: {restaurant.number_served}")



# class User:  # Defines a new class named User to represent a user profile
#     """A class representing a user profile."""  # A docstring explaining the purpose of the class

#     def __init__(
#         self, first_name, last_name, username, email
#     ):  # The constructor method to initialize a new user instance
#         self.first_name = (
#             first_name  # Stores the user's first name in an attribute
#         )
#         self.last_name = (
#             last_name  # Stores the user's last name in an attribute
#         )
#         self.username = (
#             username  # Stores the user's chosen username in an attribute
#         )
#         self.email = (
#             email  # Stores the user's email address in an attribute
#         )
#         self.login_attempts = (
#             0  # Creates a tracking attribute for login attempts, defaulting to 0
#         )

#     def describe_user(self):  # A method to print a summary of the user's profile info
#         print(
#             f"\nUser Profile Summary for {self.username}:"
#         )  # Prints a header showing which username is being described
#         print(
#             f"  Full Name: {self.first_name} {self.last_name}"
#         )  # Prints the user's combined first and last name
#         print(
#             f"  Email: {self.email}"
#         )  # Prints the email address associated with the account

#     def greet_user(self):  # A method to print a personalized welcome greeting
#         print(
#             f"Welcome back, {self.first_name}!"
#         )  # Prints a friendly message addressing the user by name

#     def increment_login_attempts(
#         self,
#     ):  # A method that increments login_attempts by 1 each time it's called
#         self.login_attempts += (
#             1  # Adds 1 to the current running total of login attempts
#         )

#     def reset_login_attempts(
#         self,
#     ):  # A method that resets the login attempts counter back to 0
#         self.login_attempts = (
#             0  # Assigns 0 back to the attribute, clearing out the old history
#         )


# # ==================== EXECUTIVE CODE ====================

# user_instance = User(
#     "Jane", "Doe", "jdoe99", "jane.doe@example.com"
# )  # Creates an instance of the User class named user_instance

# user_instance.increment_login_attempts()  # Calls the method to increment login attempts (changes from 0 to 1)
# user_instance.increment_login_attempts()  # Calls the method a second time to increment login attempts (changes from 1 to 2)
# user_instance.increment_login_attempts()  # Calls the method a third time to increment login attempts (changes from 2 to 3)
# user_instance.increment_login_attempts()  # Calls the method a fourth time to increment login attempts (changes from 3 to 4)

# print(
#     f"Login attempts after increments: {user_instance.login_attempts}"
# )  # Prints the current count to verify it incremented properly to 4

# user_instance.reset_login_attempts()  # Calls the method to clear out the count and return it back to 0

# print(
#     f"Login attempts after reset: {user_instance.login_attempts}"
# )  # Prints the count again to verify it successfully wiped back to 0
