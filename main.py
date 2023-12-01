import requests
import pandas as pd
from bs4 import BeautifulSoup

response = requests.get('https://www.binance.com/en/markets/overview')
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')
cryptos = soup.find_all(class_='css-mnze2y')

soup2 = BeautifulSoup(html_content, 'html.parser')
prices = soup.find_all(class_=['css-ny0kra', 'css-xo7uk0', 'css-1kmb4l6'])

res = {}

for crypto in cryptos:
    for price in prices:
        res[crypto.text] = price.text
        prices.remove(price)
        break

dataFrame = pd.Series(res)
dataFrame.rename('Price', inplace=True)
dataFrame.to_csv(r'C:\Users\wojtek\Pulpit\milosz\crypto_venv\cryptos.csv', index=True, header=True)


def show_menu(options):
    print("Select an option:")
    for idx, option in enumerate(options, start=1):
        print(f"{idx}. {option.text}")

    selection = input("Twój wybór (liczba): ")
    selection = int(selection)
    if 1 <= selection <= len(options):
        output = dataFrame[options[selection - 1].text]
        print("Kurs " + options[selection - 1].text + " wynosi: " + output)
    else:
        print("Niepoprawna liczba")


show_menu(cryptos)
