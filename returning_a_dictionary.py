def football_team(first_name, last_name, year=''):
    team = {'first': first_name, 'last': last_name}
    if year:
        team['year'] = year
    return team

club = football_team('bayern', 'munich', year=1972)
print(club)

while True:
    print("\nPlease what is your name? ")
    print("(enter 'q' at anytime to quit)")

    f_name = input("First name:")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    
formatted_name = football_team(f_name, l_name) 
print(f"\nHello, {formatted_name['first']} {formatted_name['last']}!")