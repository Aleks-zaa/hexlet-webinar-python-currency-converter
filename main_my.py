# 1. Приветствие
# 2. Мануал – как пользоваться программой и какие валюты доступны
# 3. Ввести исходную валюту
# 4. Ввести в какую валюту перевести
# 5. Количество валюты
# 6. Подсчёт
# 7. Вывод результата
import requests

def get_actual_currencies():
    response = requests.get(URL + API_KEY)
    res_response = response.json().get('data')
    return res_response

def convert(amount, from_currency, to_currency, currencies):
    from_value = currencies.get(from_currency)  # CURRENCIES[current_currency]
    to_value = currencies.get(to_currency)

    coefficient = to_value / from_value
    return round(amount * coefficient, 2)

def check_amount():
    i = 0
    n = ''
    while '0' not in n:
        a = input("Введите количество: ")
        while i < len(a):
            if a[i] not in NUMER:
                print('Необходимы только цифры')
                n = n + '0'
                a = input("Введите количество: ")
            n = n + '1'
            i = i + 1
        return a

URL = "https://api.freecurrencyapi.com/v1/latest?apikey="
API_KEY = "fca_live_VwM4HMSqi04e36YiIDOTyNtQSxiK8NH6frVaiI9V"
CURRENCIES = get_actual_currencies()
NUMER = {'1': '1', '2' : '2', '3' : '3', '4' : '4', '5' : '5', '6' : '6', '7' : '7', '8' : '8', '9' : '9', '0' : '0', '.' : '.'}

# 1
print("Добро пожаловать в конвертатор валют!")

# 2
print("""
Инструкция:
1. Ввести исходную валюту
2. Ввести результирующую валюту
3. Ввести количество валюты
""")

print("Доступные валюты:")

for key in CURRENCIES:
    print(f"* {key}")

def check_curr(l):
    while l not in CURRENCIES:
        print('Нет такой валюты. Выберите из списка выше ')
        l = input(" ").strip().upper()
    return l

iscur = 'Введите исходную валюту:'
rescur = 'Введите результирующую валюту:'
# 3
cc = input(iscur + " ").strip().upper()
current_currency = check_curr(cc)

# 4
rc = input(rescur + " ").strip().upper()
result_currency = check_curr(rc)

amount = check_amount()

result = convert(float(amount), current_currency, result_currency, CURRENCIES)

print(f'{amount} {current_currency} = {result} {result_currency}')
