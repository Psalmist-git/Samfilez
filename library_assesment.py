# Store all resources in a list of dictionaries.
resources = [
    {"id": "R001", "name": "Laptop", "category": "Electronics", "total": 10, "available": 10},
    {"id": "R002", "name": "Keyboard", "category": "Accessories", "total": 5, "available": 5},
    {"id": "R003", "name": "Headset", "category": "Accessories", "total": 3, "available": 3}
]

# Store fellow IDs and their names in a dictionary.
fellows = {
    "F001": "Ada",
    "F002": "John",
    "F003": "Grace"
}

# Create an empty list to store borrowing transactions.
loans = []

# Define a function for finding a resource using its ID.
def resource(rid):
    # Search through resources and return the matching resource, or None if not found.
    return next((r for r in resources if r["id"].lower() == rid.lower()), None)

# Define a function for borrowing a resource.
def borrow(fid, rid, qty):
    # Find the requested resource.
    r = resource(rid)

    # Check whether the fellow ID exists.
    if fid not in fellows:
        print("Invalid fellow.")

    # Check whether the resource exists.
    elif not r:
        print("Invalid resource.")

    # Check whether the requested quantity is valid and available.
    elif qty <= 0 or qty > r["available"]:
        print("Invalid quantity or not enough stock.")

    # Execute the borrowing operation if all checks pass.
    else:
        # Reduce the available quantity by the borrowed amount.
        r["available"] -= qty

        # Record the fellow ID, resource ID, and quantity borrowed.
        loans.append([fid, rid, qty])

        # Tell the user that borrowing was successful.
        print("Borrow successful.")

# Define a function for returning a borrowed resource.
def return_item(fid, rid, qty):
    # Find the requested resource.
    r = resource(rid)

    # Go through every recorded loan.
    for loan in loans:

        # Check whether the loan belongs to the fellow and resource.
        if loan[0] == fid and loan[1] == rid:

            # Check whether the returned quantity is valid.
            if qty <= 0 or qty > loan[2]:
                # Reject the return if the quantity is invalid.
                print("Return rejected.")

            # Process the return when the quantity is valid.
            else:
                # Reduce the amount recorded in the loan.
                loan[2] -= qty

                # Increase the resource's available quantity.
                r["available"] += qty

                # Remove the loan if everything has been returned.
                if loan[2] == 0:
                    loans.remove(loan)

                # Tell the user that the return was successful.
                print("Return successful.")

            # Stop searching after finding the matching loan.
            return

    # Display this message if no matching loan was found.
    print("No matching loan.")

# Define a function for displaying all resources.
def list_resources():
    # Go through every resource in the resources list.
    for r in resources:
        # Print the current resource.
        print(r)

# Define a function for searching resources by name.
def search():
    # Ask the user for a search word and convert it to lowercase.
    word = input("Search name: ").lower()

    # Go through every resource.
    for r in resources:
        # Check whether the search word appears in the resource name.
        if word in r["name"].lower():
            # Display the matching resource.
            print(r)

# Define a function for filtering resources by category.
def category():
    # Ask the user for a category and convert it to lowercase.
    cat = input("Category: ").lower()

    # Go through every resource.
    for r in resources:
        # Check whether the resource category matches the user's input.
        if r["category"].lower() == cat:
            # Display the matching resource.
            print(r)

# Define a function for generating a resource report.
def report():
    # Calculate the total number of resources.
    total = sum(r["total"] for r in resources)

    # Calculate the total number of currently available resources.
    available = sum(r["available"] for r in resources)

    # Display the report heading.
    print("\nREPORT")

    # Display the total number of resources.
    print("Total:", total)

    # Display the number of available resources.
    print("Available:", available)

    # Calculate and display the number of borrowed resources.
    print("Borrowed:", total - available)

    # Display the low-stock heading.
    print("Low stock:")

    # Go through every resource.
    for r in resources:
        # Check whether fewer than 3 units are available.
        if r["available"] < 3:
            # Display the resource name and available quantity.
            print(r["name"], r["available"])

    # Find the highest number of borrowed units for any resource.
    highest = max(r["total"] - r["available"] for r in resources)

    # Display the most-borrowed heading.
    print("Most borrowed:")

    # Go through every resource.
    for r in resources:
        # Calculate how many units of this resource have been borrowed.
        borrowed = r["total"] - r["available"]

        # Check whether this resource has the highest borrowing count.
        if borrowed == highest and highest > 0:
            # Display the resource name and number borrowed.
            print(r["name"], highest)

# Start the main program menu.
while True:
    # Display the available menu options.
    print("""
1. List resources
2. Borrow
3. Return
4. Search
5. Category filter
6. Report
7. Exit
""")

    # Ask the user to select a menu option.
    choice = input("Choice: ")

    # Run the resource-listing function when option 1 is selected.
    if choice == "1":
        list_resources()

    # Run the borrowing function when option 2 is selected.
    elif choice == "2":
        # Ask for the fellow ID, resource ID, and quantity to borrow.
        borrow(
            input("Fellow ID: "),
            input("Resource ID: "),
            int(input("Quantity: "))
        )

    # Run the return function when option 3 is selected.
    elif choice == "3":
        # Ask for the fellow ID, resource ID, and quantity to return.
        return_item(
            input("Fellow ID: "),
            input("Resource ID: "),
            int(input("Quantity: "))
        )

    # Run the search function when option 4 is selected.
    elif choice == "4":
        search()

    # Run the category filter when option 5 is selected.
    elif choice == "5":
        category()

    # Run the report function when option 6 is selected.
    elif choice == "6":
        report()

    # Exit the program when option 7 is selected.
    elif choice == "7":
        # Display a goodbye message.
        print("Goodbye!")

        # Stop the while loop.
        break

    # Handle any invalid menu choice.
    else:
        # Tell the user that the choice is invalid.
        print("Invalid choice.")

# Define an alternative borrowing function for demonstration.
def borrow_simple(resource, quantity):
    # Check whether the requested quantity is positive.
    if quantity <= 0:
        # Return an error message for an invalid quantity.
        return "Invalid quantity"

    # Check whether enough stock is available.
    if quantity > resource["available"]:
        # Return an error message when there is insufficient stock.
        return "Not enough stock"

    # Reduce the available stock by the requested quantity.
    resource["available"] -= quantity

    # Return a success message.
    return "Success"

# Define a function that calculates total borrowed quantities per fellow.
def total_per_fellow(transactions):
    # Create an empty dictionary for storing each fellow's total.
    totals = {}

    # Go through every transaction.
    for transaction in transactions:
        # Get the fellow's name from the transaction.
        fellow = transaction["fellow"]

        # Get the quantity from the transaction.
        quantity = transaction["quantity"]

        # Add the quantity to the fellow's existing total.
        totals[fellow] = totals.get(fellow, 0) + quantity

    # Return the completed totals dictionary.
    return totals

# Store example borrowing transactions.
transactions = [
    {"fellow": "Ada", "quantity": 2},
    {"fellow": "John", "quantity": 4},
    {"fellow": "Ada", "quantity": 3},
    {"fellow": "Grace", "quantity": 1},
    {"fellow": "John", "quantity": 2}
]

# Calculate and display the total borrowed quantity for each fellow.
print(total_per_fellow(transactions))

# Create another list containing resources and their available quantities.
resources = [
    {"name": "Laptop", "available": 0},
    {"name": "Mouse", "available": 0},
    {"name": "Keyboard", "available": 3}
]

# Keep only resources whose available quantity is not zero.
resources = [r for r in resources if r["available"] != 0]

# Display the remaining resources.
print(resources)
















#==================ASSESMENT QUESTION========================





# 1.
# Project scenario and functionality
# Learn2Earn lends equipment to fellows. Build a working Python program that stores resource inventory, issues items, accepts returns, searches inventory and produces accurate reports.

# REQUIREMENTS (70 marks):
# 1. Resource inventory (10): Every resource has unique ID, name, category, total units and available units. Add and list resources; reject duplicate IDs.
# 2. Borrowing (15): Check fellow ID and resource ID; quantity must be a positive integer and no greater than stock. Log every successful borrowing and reduce availability. Rejected attempts must not mutate state.
# 3. Returns (10): Only return quantities a fellow currently has on loan; update both borrowing records and inventory.
# 4. Search/filter (10): Case-insensitive name search; filter by category.
# 5. Reports (15): Show total units, available units, units currently borrowed, resources with fewer than 3 available units, and the resource with most units currently borrowed. If tied, identify all tied leaders.
# 6. Structure/robustness (10): Meaningful functions, menu that loops until exit, input validation and helpful errors.

# No frameworks, databases, external services, or third-party packages required. Use Python standard library only. Your application should run locally.
# Starting data
# resources = [
#   {"id": "R001", "name": "Laptop", "category": "Electronics", "total": 10, "available": 10},
#   {"id": "R002", "name": "Keyboard", "category": "Accessories", "total": 5, "available": 5},
#   {"id": "R003", "name": "Headset", "category": "Accessories", "total": 3, "available": 3}
# ]
# fellows = {"F001": "Ada", "F002": "John", "F003": "Grace"}
# borrow_records = []

# REQUIRED DEMONSTRATION, IN ORDER:
# 1. F001 borrows 2 laptops — available laptop units = 8.
# 2. F002 borrows 3 keyboards — available keyboard units = 2.
# 3. F001 returns 1 laptop — available laptop units = 9.
# 4. F003 requests 4 headsets — rejected without changing stock.
# 5. F002 tries to return 4 keyboards — rejected without changing stock.
# 6. Search for LAPtop — find Laptop, ignoring case.
# 7. Generate the report — overall units 18, available 14, borrowed 4, Keyboard low stock (2); Keyboard is most borrowed (3).

# Optional bonus, maximum 5 bonus marks outside 100: persist and reload inventory and loans using JSON.


#2.
# A2. Demonstration output and test evidence *
# 15 marks, manually graded. Paste actual run output for steps 1–7 and include one additional invalid-input test. Do not submit expected output as if you ran it.
# A3. Project design explanation *
# 5 marks, manually graded. Name at least four functions, explain how inventory and fellow loans are represented, and describe one design limitation.

# B1. Trace the code and explain the output *
# What exactly is printed, and why?

# items = [2, 4, 6]
# result = []
# for item in items:
#     if item % 4 == 0:
#         continue
#     result.append(item * 2)
# print(result)
# The exact print output is items = [4, 12]. 
# The code filters out 4 because it divides evenly by 4 leaving 0, then multiplies the remaining numbers (2 and 6) by 2, and prints the final list. Thus [4] is the only divisible number by itself, items[2, 6] will then be multiplied by *2 before printing.

# B2. Diagnose and repair a borrowing bug *
# Identify the problem, explain its consequences and rewrite the function correctly.

# def borrow(resource, quantity):
#     resource["available"] -= quantity
#     if resource["available"] < 0:
#         return "Not enough stock"
#     return "Success"

# THE PROBLEM:
# If someone tries to borrow 5 when available resources is 3;
# resource["available"] -= quantity
# stock available will be -3 leaving the inventory permanently at the negative.

# CONSEQUENCES:
# The rejected borrowing attempts will corrupt the inventory. The available stock could become negative as earlier stated.

# CORRECT FUNCTION:
# def borrow(resource, quantity):
#     if quantity <= 0:
#         return "Invalid quantity"

#     if quantity > resource["available"]:
#         return "Not enough stock"

#     resource["available"] -= quantity
#     return "Success"

# B3. Aggregate transaction data *
# Write a function that returns a dictionary of the total quantity per fellow, without hardcoding results.

# transactions = [
#     {"fellow": "Ada", "quantity": 2},
#     {"fellow": "John", "quantity": 4},
#     {"fellow": "Ada", "quantity": 3},
#     {"fellow": "Grace", "quantity": 1},
#     {"fellow": "John", "quantity": 2}
# ]

# Expected totals: Ada 5; John 6; Grace 1.
# def total_per_fellow(transactions):
#     totals = {}

#     for transaction in transactions:
#         fellow = transaction["fellow"]
#         quantity = transaction["quantity"]

#         totals[fellow] = totals.get(fellow, 0) + quantity

#     return totals


# transactions = [
#     {"fellow": "Ada", "quantity": 2},
#     {"fellow": "John", "quantity": 4},
#     {"fellow": "Ada", "quantity": 3},
#     {"fellow": "Grace", "quantity": 1},
#     {"fellow": "John", "quantity": 2}
# ]

# print(total_per_fellow(transactions))

# B4. Mutating a list during iteration *
# Will the code always remove every unavailable resource? Explain and provide a reliable correction.

# resources = [
#     {"name": "Laptop", "available": 0},
#     {"name": "Mouse", "available": 0},
#     {"name": "Keyboard", "available": 3}
# ]
# for resource in resources:
#     if resource["available"] == 0:
#         resources.remove(resource)
# print(resources)
# - No the code may not always remove every unavailable resources.
# - You should not remove items from a list while looping through it because Python may skip some items.

# resources = [
#     {"name": "Laptop", "available": 0},
#     {"name": "Mouse", "available": 0},
#     {"name": "Keyboard", "available": 3}
# ]

# resources = [r for r in resources if r["available"] != 0]

# print(resources)

# B5. Reason about simultaneous requests *
# Inventory has five available laptops. Two fellows request four each at nearly the same time. Why can a separate stock check and stock update be unsafe if requests execute concurrently? Describe a method to ensure no more laptops are issued than available. No code required.
# Ans:
# If there are only 5 laptops available and two people request 4 laptops each at the same time, both requests might check the stock before either one updates it. Both may see 5 laptops available and receive 4, causing 8 laptops to be issued when only 5 exist.

# To prevent this, the stock check and stock update should happen as one single operation. The system should lock the stock while checking and updating it. This ensures that one request is completed before the next request checks the available stock.

# B6. Defend your own implementation *
# Answer all three: (a) What was the most challenging project feature and how did you solve it? (b) Describe a bug you encountered, how you found it and how you fixed it. (c) What would you improve first if 500 fellows used the system, and why?
# Ans:
# A. The most challenging part was managing borrowing and returning items correctly. I had to make sure fellows could only borrow items that were available. I solved this by checking the fellow ID, resource ID, and available stock before updating the records.
# B. I found a problem where two people could request the same items at almost the same time. This could cause more items to be given out than were available. I found it by testing several requests together. I fixed it by making the stock check and stock update happen together, so the inventory always stays correct.
# C. I would first improve the system to handle many users at the same time. This would help prevent errors when many fellows borrow or return items at once. I would also add data saving so that the inventory and borrowing records are not lost when the program closes.