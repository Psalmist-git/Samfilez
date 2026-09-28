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
