def ticket_total(price, quantity):
    return price * quantity

amount = ticket_total(9, 2)
print(amount)

def passing_scores(scores):
    passed = []
    for index in range(len(scores)):
        if scores[index] >= 50:
            passed.append(scores[index])
    return passed

print(passing_scores([49, 50, 80, 65]))


# assert passing_scores([50]) ==, "Failed to include the exact boundary score of 50"

# assert passing_scores([85]) ==, "Failed to include a single passing score above 50"

# assert passing_scores([]) == [], "Failed to return an empty list when given an empty list"
