# 1. Приветствие
# 2. Мануал – как пользоваться программой и какие валюты доступны
# 3. Ввести исходную валюту
# 4. Ввести в какую валюту перевести
# 5. Количество валюты
# 6. Подсчёт
# 7. Вывод результата

import requests
URL = "https://api.freecurrencyapi.com/v1/latest?apikey="
API_KEY = "fca_live_VwM4HMSqi04e36YiIDOTyNtQSxiK8NH6frVaiI9V"
def get_actual_currencies():
    response = requests.get(URL + API_KEY)
    return response.json()

CURRENCIES = get_actual_currencies()

print(CURRENCIES)
def convert(amount, from_currency, to_currency, currencies):
    from_value = currencies.get(from_currency)  # CURRENCIES[current_currency]
    to_value = currencies.get(to_currency)

    coefficient = to_value / from_value
    return round(amount * coefficient, 2)
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

for key in CURRENCIES['data']:
    print(f"* {key}")

# 3
current_currency = input("Введите исходную валюту: ").upper()
while current_currency not in CURRENCIES['data']:
    print('Нет такой валюты')
    current_currency = input("Введите исходную валюту: ").upper()
# 4
result_currency = input("Введите результирующую валюту: ").upper()
while result_currency not in CURRENCIES['data']:
    print('Нет такой валюты')
    result_currency = input("Введите результирующую валюту: ").upper()

# 5
amount = input("Введите количество: ")


# 6
result = convert(float(amount), current_currency, result_currency, CURRENCIES['data'])

print(f'{amount} {current_currency} = {result} {result_currency}')
