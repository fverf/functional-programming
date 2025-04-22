#параллельное вычисление суммы элементов списка с использованием pmap

import concurrent.futures

def parallel_sum(numbers):
    with concurrent.futures.PoolExecutor() as executor:
        return sum(executor.map(lambda x: x, numbers))

numbers = [1, 2, 3, 4, 5, 6]
print(parallel_sum(numbers))