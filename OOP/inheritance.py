class Vehicle:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f'''
Make: {self.make}
Model: {self.model}
Year: {self.year}
''')
        
# vehicle1 = Vehicle('Ford','Focus',2013)
# vehicle1.display_info()

class Car(Vehicle):
    def __init__(self, make, model, year, number_of_doors):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors

    def display_info(self):
        super().display_info()
        print(f'Number of doors: {self.number_of_doors}')

# car1 = Car('Ford','Focus',2013,4)
# car1.display_info()

class Bike(Vehicle):
    def __init__(self, make, model, year,type_of_bike):
        super().__init__(make,model,year)
        self.type_of_bike = type_of_bike

    def display_info(self):
        super().display_info()
        print(f'Type of bike: {self.type_of_bike}')

bike1 = Bike('make','model','year','bike type')
bike1.display_info()

class Truck(Vehicle):
    def __init__(self, make, model, year,payload_capacity):
        super().__init__(make,model,year)
        self.payload_capacity = payload_capacity
        self.payload_capacity = float(self.payload_capacity)

    def display_info(self):
        super().display_info()
        print(f'Payload Capacity: {self.payload_capacity}')

truck1 = Truck('make','model','year',99.99)
truck1.display_info()