class Phones():

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.battery_level = 0  # Fixed: Renamed attribute to prevent conflict with method name

    def get_discritive_name(self):
        long_name = str(self.year) + ' ' + self.brand + ' ' + self.model
        return long_name.title()

    def charge_percentage(self):
        print("This phone has a " + str(self.battery_level) + " percent charge on it.")

    def update_percentage(self, percent):
        if percent >= self.battery_level:
            self.battery_level = percent
        else:
            print("You can't use a flat phone!")

    def increment_percentage(self, percent):
        self.battery_level += percent


class PoshPhone(Phones):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)

    # Fixed: Placed the block inside the class and corrected attribute references
    def charge_percentage(self):
        self.battery_level = 100
        print("This phone has a " + str(self.battery_level) + " percent charge on it.")


# --- Execution ---
my_device = PoshPhone('apple', 'iphone 13', 2025)
print(my_device.get_discritive_name())

# Call the fixed method
my_device.charge_percentage()

from phones import PoshPhone

my_device = PoshPhone('apple', 'iphone 13', 2025)

print(my_device.get_discritive_name())
my_device.charge_percentage()

# 4. Correct way to view or access the battery level attribute directly
print(f"Direct battery level read: {my_device.battery_level}%")



from phones import Phones, PoshPhone

my_phone = Phones('samsung', 'tecno', 2020)
print(my_phone.get_discritive_name())

my_connect = PoshPhone('iphone 13', 'pro', 2025)
print(my_connect.get_discritive_name())

import phones

my_phone = phones.Phones('samsung', ' duo', 2020)
print(my_phone.get_discritive_name())

my_connect = phones.PoshPhone('iphone 13', 'pro', 2025)
print(my_connect.get_discritive_name())