import requests

# URL for CoinDesk's Bitcoin Price API
url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"

# Sending request
response = requests.get(url)

# Parse JSON response
if response.status_code == 200:
    data = response.json()
    bitcoin_price = data['bpi']['USD']['rate']
    print("Current Bitcoin price in USD:", bitcoin_price)
else:
    print("Error:", response.status_code)
