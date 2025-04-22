#тесты для функции факториала
import pytest
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def test_factorial_base():
    assert factorial(0) == 1
    assert factorial(1) == 1

def test_factorial_regular():
    assert factorial(5) == 120
    assert factorial(7) == 5040


#тесты для функции длины строки
def string_length(s):
    return len(s)

def test_string_length():
    assert string_length("") == 0
    assert string_length("куку") == 5
    assert string_length(" ") == 1


#фикстуры для инициализации данных

@pytest.fixture
def sample_data():
    return ["яблоки", "вишня", "бананы"]

def test_sample_length(sample_data):
    assert len(sample_data) == 3

def test_first_item(sample_data):
    assert sample_data[0] == "яблоки"
