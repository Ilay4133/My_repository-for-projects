#ИНКАПСУЛЯЦИЯ (пример №1)
class RAM:
    def __init__(self, name, frequency):
        self.__name = name  # устанавливаем имя
        self.__frequency = frequency

    @property
    def frequency(self):
        return self.__frequency

    # свойство-сеттер
    @frequency.setter
    def frequency(self, frequency):
        if 4800 < frequency < 8400:
            self.__frequency = frequency
        else:
            print("Недопустимая частота")

    def Print_ram(self):
        print(f"Название: {self.__name}\tЧастота: {self.__frequency}")

ram1=RAM("ADATA XPG ddr5",4808)

ram1.Print_ram()
ram1.frequency=59875432
ram1.frequency=5600
ram1.Print_ram()
ram1.frequency=1746
ram1.frequency=8300
ram1.Print_ram()


#ИНКАПСУЛЯЦИЯ (пример №2)

#ИНКАПСУЛЯЦИЯ (пример №1)
class Tiger:
    def __init__(self, name, age):
        self.__name = name  # устанавливаем имя
        self.__age = age

    @property
    def age(self):
        return self.__age

    # свойство-сеттер
    @age.setter
    def frequency(self, age):
        if 0 < age < 20:
            self.__age = age
        else:
            print("Недопустимый возраст")

    def Print_ram(self):
        print(f"Имя: {self.__name}\tВозраст: {self.__age}")

tiger1=Tiger("Persick",12)

tiger1.Print_ram()
tiger1.frequency=59
tiger1.frequency=5
tiger1.Print_ram()
tiger1.frequency=6.7
tiger1.frequency=-4
tiger1.Print_ram()
