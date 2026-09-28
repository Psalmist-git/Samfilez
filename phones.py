class Phones():
    def __init__(self, brand, model, year ):
        self.brand = brand
        self.model = model
        self.year = year
        self.charge_percentage = 0

    def get_discritive_name(self):
        long_name = str(self.year) + ' ' + self.brand + ' ' + self.model
        return long_name.title()

    def charge_percentage(self):
        print("This phone has a " + str(self.charge_percentage) + " percent charge on it.")

    def update_percentage(self, percent):
        if percent >= self.charge_percentage:
            self.charge_percentage = percent
        else:
            print("You can't use a flat phone!")

    def increment_percentage(self, percent):
        self.charge_percentage += percent

class PoshPhone(Phones):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)

my_device = PoshPhone('apple', 'iphone 13', 2025)
print(my_device.get_discritive_name())