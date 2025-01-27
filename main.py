import requests

# Ваш API-ключ
api_key = "CPTJE7N20FY78PYP"

# Параметры запроса
function = "CURRENCY_EXCHANGE_RATE"
from_currency = "USD"
to_currency = "EUR"

# Формируем URL
url = f"https://www.alphavantage.co/query?function={function}&from_currency={from_currency}&to_currency={to_currency}&apikey={api_key}"

# Выполняем запрос
response = requests.get(url)
data = response.json()

# Выводим результат
print(data)