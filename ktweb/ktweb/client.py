import requests

BASE_URL = 'http://localhost:5000'
def menu():
    while True:
        print("\nдействие:")
        print("1. создать")
        print("2. показать")
        print("3. изменить")
        print("4. удалить")
        print("5. выйти")
        choice = input("номер: ")

        if choice == '1':
            url = input("введите URL: ")
            response = requests.post(f"{BASE_URL}/normal-url", json={'url': url})
            if response.status_code == 200:
                print("короткий URL:", response.json()['short_url'])
            else:
                print("ошибка при создании URL")

        elif choice == '2':
            short_url = input("введите короткий URL: ")
            response = requests.get(f"{BASE_URL}/short-url/{short_url}")
            if response.status_code == 200:
                print("URL:", response.json()['url'])
            else:
                print("URL не найден")

        elif choice == '3':
            short_url = input("введите короткий URL: ")
            new_url = input("введите новый URL: ")
            response = requests.put(f"{BASE_URL}/short-url/{short_url}", json={'url': new_url})
            if response.status_code == 200:
                print("URL обновлен")
            else:
                print("не удалось обновить URL")

        elif choice == '4':
            short_url = input("введите короткий URL: ")
            response = requests.delete(f"{BASE_URL}/short-url/{short_url}")
            if response.status_code == 200:
                print("URL удален")
            else:
                print("не удалось удалить URL")

        elif choice == '5':
            print("выход")
            break
        else:
            print("попробуйте снова")

if __name__ == '__main__':
    menu()