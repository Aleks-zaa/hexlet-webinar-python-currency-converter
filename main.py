# 1. Приветствие
# 2. Мануал – как пользоваться программой и какие валюты доступны
# 3. Ввести исходную валюту
# 4. Ввести в какую валюту перевести
# 5. Количество валюты
# 6. Подсчёт
# 7. Вывод результата

CURRENCIES = {
    "USD": {
        "value": 1,
        "label": "Доллар США",
    },
    "RUB": {
        "value": 96.25,
        "label": "Российский Рубль",
    },
    "EUR": {
        "value": 0.93,
        "label": "Евро",
    },
    "KZT": {
        "value": 466.24,
        "label": "Казахстанский Тенге",
    },
}


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

for key in CURRENCIES:
    currency = CURRENCIES.get(key)

    print(f'* {key} - {currency.get("label")}')

# 3
current_currency = input("Введите исходную валюту: ")
# 4
result_currency = input("Введите результирующую валюту: ")
# 5
amount = input("Введите количество: ")

# 6
formatted_currencies = {}
for key in CURRENCIES:
    formatted_currencies[key] = CURRENCIES.get(key).get("value")

result = convert(float(amount), current_currency, result_currency, formatted_currencies)

print(f'{amount} {current_currency} = {result} {result_currency}')
