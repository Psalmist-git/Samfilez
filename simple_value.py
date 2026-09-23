def make_shirt(shirt_size, text_print):
    print(f"\nI have a " + shirt_size + ".")
    print("My " + shirt_size + "'s front print is " + text_print.title() + ".")

make_shirt('large calvin cline T.shirt','We are the HER for tommorow.')



def get_details(first_name, middle_name, last_name):

    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

artist = get_details('Burna', 'Damini', 'ogulu')
print(artist)



def get_details(first_name, last_name, middle_name=''):

    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

artist = get_details('Burna', 'Damini')
print(artist)

artist = get_details('Burna', 'damini', 'ogulu')
print(artist)
