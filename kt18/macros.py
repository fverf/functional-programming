#макрос для логирования начала и конца выполнения
import functools
import logging
from xml.etree.ElementTree import PI

logging.basicConfig(level=logging.INFO)
def with_logging(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Starting {func.__name__}...")
        result = func(*args, **kwargs)
        logging.info(f"Finished {func.__name__}.")
        return result
    return wrapper

@with_logging
def example_function(x, y):
    return x + y

print(example_function(3, 4))


#макрос для проверки равенства двух значений
def assert_equal(a, b):
    if a != b:
        raise AssertionError(f"фейл{a} != {b}")
    else:
        print(f"успешно {a} == {b}")

assert_equal(5, 5)
assert_equal(3, 4)


#макрос для создания константы
def defconstant(name, value):
    globals()[name] = value

defconstant('PI', 3.14159)
print(PI)