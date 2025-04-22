# Реализуйте объект "машина" с методами для ускорения, торможения и получения текущей скорости

def create_car():
    speed = [0]
    def car(method, *args):
        match method:
            case 'accelerate':
                speed[0] += args[0]
            case 'brake':
                speed[0] = max(0, speed[0] - args[0])
            case 'get_speed':
                return speed[0]
    return car

car = create_car()
car('accelerate', 50)
car('brake', 20)
print(car('get_speed'))

# 2. Создайте объект "библиотека", который хранит список книг и позволяет добавлять, удалять и искать книги
def create_library():
    books = []
    def library(method, *args):
        match method:
            case 'add':
                books.append(args[0])
            case 'remove':
                books.remove(args[0])
            case 'find':
                return list(filter(lambda b: args[0].lower() in b.lower(), books))
            case 'all':
                return books
    return library

lib = create_library()
lib('add', 'крутая книжка 1')
lib('add', 'крутая книжка 2')
lib('add', 'крутая книжка 3')
lib('remove', 'крутая книжка 2')
print(lib('find', 'peace'))
print(lib('all'))


# 3. Реализуйте объект "банк", который содержит несколько счетов и позволяет переводить деньги между ними
def create_bank():
    accounts = {}
    def bank(method, *args):
        match method:
            case 'create':
                name, balance = args
                accounts[name] = balance
            case 'transfer':
                from_acc, to_acc, amount = args
                if accounts[from_acc] >= amount:
                    accounts[from_acc] -= amount
                    accounts[to_acc] += amount
            case 'balance':
                return accounts[args[0]]
    return bank

bank = create_bank()
bank('create', 'Леся', 500)
bank('create', 'Вовка', 300)
bank('transfer', 'Леся', 'Вовка', 200)
print(bank('balance', 'Леся'))
print(bank('balance', 'Вовка'))