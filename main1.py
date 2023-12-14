def dekorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrapper

@dekorator
def numbers(a, b):
    return a + b

result = numbers(3, 4)
print(result)