import logging
import random

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('toyotas.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

class ToyotaCar:
    def __init__(self, model, year, color, mileage, fuel_type):
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage
        self.fuel_type = fuel_type
        self.engine_status = 'off'
        self.speed = 0
        
        
        logger.info(f"Created Toyota: {self.year} Toyota {self.model}")
        
    def start_engine(self):
        if self.engine_status == 'off':
            self.engine_status = 'on'
            print("Engine started.")
        else:
            print("Engine is already running.")
        
    def stop_engine(self):
        if self.engine_status == 'on':
            self.engine_status = 'off'
            self.speed = 0
            print("Engine stopped.")
        else:
            print("Engine is already off.")
        
    def accelerate(self, speed_increment):
        if self.engine_status == 'on':
            self.speed += speed_increment
            print(f"Accelerated to {self.speed} km/h.")
        else:
            print("Cannot accelerate. Engine is off.")
        
    def brake(self, speed_decrement):
        if self.engine_status == 'on':
            if self.speed >= speed_decrement:
                self.speed -= speed_decrement
                print(f"Braked to {self.speed} km/h.")
            else:
                self.speed = 0
                print("Car has come to a stop.")
        else:
            print("Cannot brake. Engine is off.")
        
    def display_info(self):
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")
        print(f"Mileage: {self.mileage} km")
        print(f"Fuel Type: {self.fuel_type}")
        print(f"Engine Status: {self.engine_status}")
        print(f"Current Speed: {self.speed} km/h")


toyota_models = ["Camry", "Corolla", "RAV4", "Highlander", "Prius", 
                 "Sienna", "Tacoma", "Tundra", "C-HR", "Yaris", "Supra", "Land Cruiser"]

years = list(range(1999, 2021))

mileage = [0, 10000, 20000, 50000, 75000, 100000, 150000, 200000, 250000, 300000]
car_colors = ["Black", "White", "Silver", "Gray", "Red", "Blue", "Green", "Yellow",
              "Orange", "Purple", "Brown", "Beige"]

fuel_types = ["Gasoline", "Diesel", "Electric", "Hybrid", "Ethanol", "LPG (Liquefied Petroleum Gas)", 
              "CNG (Compressed Natural Gas)", "Hydrogen"]



toyota_car = ToyotaCar(random.choice(toyota_models), random.choice(years), random.choice(car_colors)
                       ,random.choice(mileage), random.choice(fuel_types))

toyota_car.display_info()

toyota_car.start_engine()
toyota_car.accelerate(50)
toyota_car.brake(20)
toyota_car.stop_engine()
