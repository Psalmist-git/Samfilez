# ==========================================
# 1. THE CLASS DEFINITION
# ==========================================
class AnonymousSurvey:  # Defines a new blueprint template called AnonymousSurvey for creating survey objects.
    """Collect anonymous answers to a survey question."""  # A docstring explaining the purpose of this class to other coders.

    def __init__(self, question):  # The constructor method that initializes data fields whenever a new survey is made.
        """Store a question, and prepare to store responses."""  # A docstring explaining that this method sets up initial survey data.
        self.question = question  # Stores the incoming question string inside the object's personal data profile.
        self.responses = []  # Creates an empty list inside the object to keep track of incoming survey answers.

    def show_question(self):  # Defines a method function to display the stored survey question.
        """Show the survey question."""  # A docstring explaining what this specific method accomplishes.
        print(self.question)  # Outputs the survey question text directly to the console or terminal window.

    def store_response(self, new_response):  # Defines a method function that accepts and saves a single new answer.
        """Store a single response to the survey."""  # A docstring explaining that this method adds a response to our data storage.
        self.responses.append(new_response)  # Takes the new answer string and appends it to the end of the responses list.

    def show_results(self):  # Defines a method function to print out all the collected answers.
        """Show all the responses that have been given."""  # A docstring explaining the final output function of the class.
        print("Survey results:")  # Prints a clean section header text to introduce the results list.
        for response in self.responses:  # Loops through every individual answer string saved inside the responses list.
            print(f"- {response.title()}")  # Prints each individual answer with a clean bullet point layout.


# ==========================================
# 2. THE INTERACTIVE PROGRAM EXECUTION
# ==========================================
# Define the question and create the survey object
question = "What language did you first learn to speak?"  # Creates a string variable containing the core polling question.
my_survey = AnonymousSurvey(question)  # Instantiates a real live object from the blueprint class using our question string.

# Display the question and instructions
my_survey.show_question()  # Commands our new survey object to call its method and display the question text.
print("Enter 'q' at any time to quit or exit.\n")  # Prints user operating instructions so participants know how to close the app.

# Start a loop to collect responses
while True:  # Commences an infinite loop structure that will keep running until explicitly broken.
    response = input("Language: ")  # Pauses execution to wait for a user to type their response into the terminal console.
    if response.lower() == 'q':  # Checks if the user typed the letter 'q' (automatically converting capitals to lowercase).
        break  # Snaps out of the infinite loop immediately if the quit command condition matches.
    my_survey.store_response(response)  # Sends the valid language string to our object's storage array if they didn't quit.

# Show the collected results
print("\nThank you to everyone who participated in this survey.")  # Outputs a polite appreciation message once data collection stops.
my_survey.show_results()  # Runs the final object method to display every single response gathered during runtime.
