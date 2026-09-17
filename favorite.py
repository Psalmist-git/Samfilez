favorite_color = {
    'law': 'white',
    'cheke': 'black',
    'akyenyi': 'blue',
    'chuba': 'green',
}
print("cheke's favorite color is " + favorite_color['cheke'].title() + ".")
print("law's favorite color is " + favorite_color['law'].title() + ".")
print("akyenyi's favorite color is " + favorite_color['akyenyi'].title() + ".")
print("chuba's favorite color is " + favorite_color['chuba'].
title() + ".")

for name in favorite_color.keys():
    print(name.title())

for name, color in favorite_color.items():
    print(name.title() + "'s favorite color is " + color.title() + ".")

friends = ['law', 'cheke']
for name in favorite_color.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() + ", i see your favorite color is " + favorite_color[name].title() + "!")

    if 'yankis'.title() not in favorite_color.keys():
        print("Yankis, please select a color!")

for name in sorted(favorite_color.keys()):
    print(name.title() + ", thank you for sticking to your color.")

print("The following colors have been mentioned:")
for color in favorite_color.values():
    print(color.title())
