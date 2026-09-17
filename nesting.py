ligue_1 = {'club': 'PSG', 'points': 10}
laliga = {'club': 'madrid', 'points': 15}
premier = {'club': 'chelsea', 'points': 100}

leagues = [ligue_1, laliga, premier]

for league in leagues:
    print(league)

leagues = []

for league in range(30):
    new_league = {'club': 'PSG', 'points': 10}
    leagues.append(new_league)

for league in leagues[:10]:
    print(league)
print("...")

print("Total number of clubs: " + str(len(leagues)))

# FIX 1: Use the loop variable 'league' instead of the list 'leagues'
# FIX 2: Removed illegal trailing colons and corrected assignment logic
for league in leagues[0:3]:
    if league['club'] == 'PSG':
        league['club'] = 'madrid'
        # Note: Reassigning the key right away overrides 'madrid' to 'chelsea'
        league['club'] = 'chelsea'
        # points are stored as integers in previous lines, changing to string '10' here
        league['points'] = '10'

# FIX 3: Changed 'clubs' to 'leagues' since 'clubs' was never defined
for club in leagues[0:5]:
    print(club)
print("...")
