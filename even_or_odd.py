number = input("Enter a number and i will tell you if its even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe numner " + str(number) + " is even.")

else:
    print("\nThe number " + str(number) + " is odd.")