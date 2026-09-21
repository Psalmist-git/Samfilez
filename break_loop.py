promt = "\nPlease enter the name of the city you have visited:"
promt += "\n(Enter 'quit' when you are finished.) "

active = True
while True:
    city = input(promt) 
    
    if city ==  'quit':
        break
    else:
        print("I would love to visit " + city.title() + "!")