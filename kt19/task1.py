#атом, который хранит список чисел, и добавление новых чисел

import threading

class Atom:
    def __init__(self, value):
        self._value = value
        self._lock = threading.Lock()

    def update(self, func):
        with self._lock:
            self._value = func(self._value)

    def get(self):
        with self._lock:
            return self._value

atom = Atom([])

def add_number(num):
    atom.update(lambda x: x + [num])

add_number(5)
add_number(10)

print(atom.get())