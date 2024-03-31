#АБСТРАКТНЫЕ КЛАССЫ (пример №1)
import abc
number1 = int(input("Первое число:"))
number2 = int(input("Второе число:"))
class Shape(abc.ABC):
    @abc.abstractmethod
    def answer (self): pass
class Sum(Shape):
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
    def answer(self):
        return self.number1 + self.number2
class Residual(Shape):
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
    def answer(self):
        return self.number1 - self.number2
class Multiplication(Shape):
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
    def answer(self):
        return self.number1 * self.number2
class Separation1(Shape):
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
    def answer(self):
        return self.number1 / self.number2
class Separation2(Shape):
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
    def answer(self):
        return self.number1 // self.number2

answer1=Sum(number1, number2)
answer2=Residual(number1, number2)
answer3=Multiplication(number1, number2)
answer4=Separation1(number1, number2)
answer5=Separation2(number1, number2)

print("Сложение:", answer1.answer())
print("Вычитание:",answer2.answer())
print("Умножение:",answer3.answer())
print("Деление:",answer4.answer())
print("Целочисленное деление:",answer5.answer())


#АБСТРАКТНЫЕ КЛАССЫ (пример №2)
import abc
class Book(abc.ABC):
    @abc.abstractmethod
    def info (self): pass
class Roman(Book):
    def __init__(self, author, age, name):
        self.author = author
        self.age = age
        self.name=name
        self.type="роман"
    def info(self):
        print(f"Это {self.type}: {self.name}, автор: {self.author}, написанный в: {self.age}")
class Novel(Book):
    def __init__(self, author, age, name):
        self.author = author
        self.age = age
        self.name=name
        self.type="повесть"
    def info(self):
        print(f"Это {self.type}: {self.name}, автор: {self.author}, написанная в: {self.age}")
class Story(Book):
    def __init__(self, author, age, name):
        self.author = author
        self.age = age
        self.name=name
        self.type="рассказ"
    def info(self):
        print(f"Это {self.type}: {self.name}, автор: {self.author}, написанный в: {self.age}")
class Poem(Book):
    def __init__(self, author, age, name):
        self.author = author
        self.age = age
        self.name=name
        self.type="поэма"
    def info(self):
        print(f"Это {self.type}: {self.name}, автор: {self.author}, написанная в: {self.age}")

book1 = Poem("А.С. Красников", 1934, "Алая луна")
book2 = Story("А.С. Пушкин", 1876, "Туча")
book3 = Roman("А.Т. Морьян", 2001, "Рассвет")
book4 = Novel("нет информации", 1934, "Боль")
book1.info()
book2.info()
book3.info()
book4.info()
