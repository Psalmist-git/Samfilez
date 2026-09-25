class FootballPlayer():                          # Defines the blueprint (class) for creating football player objects
    def __init__(self, name, position, club, girlfriend='Bianca_Jacobson'):  # Initializer function with a default girlfriend argument
        self.girlfriend = girlfriend              # Stores the girlfriend's name string in the object's attribute
        self.name = name                          # Stores the player's name string in the object's attribute
        self.position = position                  # Stores the tactical position string in the object's attribute
        self.club = club                          # Stores the current football club string in the object's attribute
        self.stats = {'goals': 41, 'assists': 28, 'yellow_cards': 0, 'red_cards': 0, 'speed': 90, 'strength': 80, 'stamina': 85 }  # Stores player metrics inside a dictionary attribute

    def describe_player(self):                    # Defines a method (action) to display all stored data about the player
        print("Player Name: " + self.name.title())  # Capitalizes and prints the player's name
        print("Position: " + self.position.title())  # Capitalizes and prints the player's position
        print("Club: " + self.club.title())       # Capitalizes and prints the player's club name
        print("Goals: " + str(self.stats['goals']))  # Converts the goals dictionary number to text and prints it
        print("Assists: " + str(self.stats['assists']))  # Converts the assists dictionary number to text and prints it
        print("Yellow Cards: " + str(self.stats['yellow_cards']))  # Converts yellow cards to text and prints it
        print("Red Cards: " + str(self.stats['red_cards']))  # Converts red cards to text and prints it
        print("Speed: " + str(self.stats['speed']))  # Converts speed metric to text and prints it
        print("Strength: " + str(self.stats['strength']))  # Converts strength metric to text and prints it
        print("Stamina: " + str(self.stats['stamina']))  # Converts stamina metric to text and prints it
        print("Girlfriend: " + self.girlfriend.title())  # Capitalizes and prints the girlfriend's name attribute
        print("_" * 30)                           # Prints a clean horizontal divider line using 30 underscores


the_player = FootballPlayer('cole palmer', 'central attacking midfielder', 'chelsea fc')  # Creates an instance of the class for Cole Palmer with his position and club
the_player.describe_player()                      # Executes the describe_player method to print all of Cole Palmer's details to the screen
