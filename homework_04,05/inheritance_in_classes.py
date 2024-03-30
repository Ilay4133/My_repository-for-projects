#НАСЛЕДСТВО (пример №1)
class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"Это {self.name}, ему {self.age} лет.")
    def peculiarities(self):
        print("У кошачьих: голова небольшая, а туловище очень стройное, изящное. Ноги не высокие, но мощные. "
              "Когти полностью или частично втягиваются.")
class Tiger(Cat):
    pass
class Cheetah(Cat):
    pass
class Puma(Cat):
    pass

Leo=Tiger("Leo",12)
Dero=Cheetah("Dero",19)
Raw=Puma("Raw",1)

Leo.info()
Leo.peculiarities()
Dero.info()
Dero.peculiarities()
Raw.info()
Raw.peculiarities()

#НАСЛЕДСТВО (пример №2)
#НАСЛЕДСТВО (пример №1)
class Train:
    def __init__(self,num,wheels, vagons):
        self.num=num
        self.wheels=wheels
        self.vagons=vagons
    def info(self):
        print(f"Это поезд номер: {self.num}, у него{self.wheels} колес. В нем {self.vagons}")
class Tram(Train):
    pass
class Freight_train(Train):
    pass
class Passenger_train(Train):
    pass

Leo=Tram("134",8, 2)
Dero=Freight_train("7774",12,154)
Raw=Passenger_train("344",8,23)

Leo.info()
Dero.info()
Raw.info()

