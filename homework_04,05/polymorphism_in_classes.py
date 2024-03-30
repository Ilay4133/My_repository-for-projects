#ПОЛИМОРФИЗМ (пример №1)
class СPU_info:
    def __init__(self, name, age, memory, connector):
        self.name = name
        self.age = age
        self.memory = memory
        self.connector = connector
class CPU(СPU_info):
    def info(self):
        print(f"name: {self.name}, age: {self.age}, memory: {self.memory}, connector: {self.connector}")
class GPU_info:
    def __init__(self, name, age, memory, bits):
        self.name = name
        self.age = age
        self.memory = memory
        self.bits = bits
class GPU(GPU_info):
    def info(self):
        print(f"name: {self.name}, age: {self.age}, memory: {self.memory}, cuda: {self.bits}")

cpu1=CPU("I7 12400", 2020,  "DDR4 (до 3200 МГц) и DDR5 (до 5600 МГц)", "LGA 1700")
cpu2=CPU("I9 10400", 2019,  "DDR4 (до 2666 МГц)", "LGA 1200")
gpu1=GPU("RTX 2060 12gb", 2019,  "12Gb/GDDR6 14000Mhz", "192")
gpu2=GPU("RTX 4070 TI", 2024,  "12Gb/GDDR6X 21000Mhz", "cuda: 7680")

for processing in (cpu1, cpu2, gpu1, gpu2):
    processing.info()

#ПОЛИМОРФИЗМ (пример №2)
class Truck:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def info(self):
        print(f"Name: {self.name}, age: {self.age}, color: {self.color}")

    def make_sound(self):
        print("beeeeeb")


class Car:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def info(self):
        print(f"Name: {self.name}, age: {self.age}, color: {self.color}")

    def make_sound(self):
        print("bib bib")


truck1 = Truck("Ural-4320", 1977, "military green")
car1 = Car("Porsche 911", 2019, "red")

for cars in (truck1, car1):
    cars.make_sound()
    cars.info()
    cars.make_sound()

