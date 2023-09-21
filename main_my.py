import requests

URL = "https://api.freecurrencyapi.com/v1/latest?apikey="
API_KEY = "fca_live_VwM4HMSqi04e36YiIDOTyNtQSxiK8NH6frVaiI9V"
NUMER = {'1': '1', '2' : '2', '3' : '3', '4' : '4', '5' : '5', '6' : '6', '7' : '7', '8' : '8', '9' : '9', '0' : '0', '.' : '.'}

# Функции
def get_actual_currencies():
    response = requests.get(URL + API_KEY)
    res_response = response.json().get('data')
    return res_response

def convert(amount, from_currency, to_currency, currencies):
    from_value = currencies.get(from_currency)  # CURRENCIES[current_currency]
    to_value = currencies.get(to_currency)

    coefficient = to_value / from_value
    return round(amount * coefficient, 2)

def check_curr(value):
    while value not in CURRENCIES:
        print('Нет такой валюты. Выберите из списка выше ')
        value = input(" ").strip().upper()
    return value
def check_amount():
    i = 0
    n = ''
    while '0' not in n:
        value = input("Введите количество: ")
        while i < len(value):
            if value[i] not in NUMER:
                print('Необходимы только цифры')
                n = n + '0'
                value = input("Введите количество: ")
            n = n + '1'
            i = i + 1
        return value

# Исполняемая часть
print("Добро пожаловать в конвертатор валют!")

print("Доступные валюты:")
CURRENCIES = get_actual_currencies()
for key in CURRENCIES:
    print(f"* {key}")

current_currency = check_curr(input('Введите исходную валюту: ').strip().upper())
result_currency = check_curr(input('Введите результирующую валюту: ').strip().upper())

amount = check_amount()

result = convert(float(amount), current_currency, result_currency, CURRENCIES)

print(f'{amount} {current_currency} = {result} {result_currency}')
