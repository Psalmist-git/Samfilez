def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

artist = get_formatted_name('burna boy', 'ogulu')
print(artist)


def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()

artist = get_formatted_name('burna boy', 'damini', 'ogulu')
print(artist)


