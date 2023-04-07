def cast(result_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return result_type(result)
            except ValueError:
                raise ValueError("Некоректный тип")
        return wrapper
    return decorator

@cast(float)
def multiply(a, b):
    return a * b

result = multiply(2, 3)
print(result)

result = multiply(2, "3")
print(result)
