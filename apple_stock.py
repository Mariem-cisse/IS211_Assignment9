
import requests
from bs4 import BeautifulSoup

# Yahoo Finance Apple stock history
url = "https://finance.yahoo.com/quote/AAPL/history/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers, timeout=20)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table")

if table:
    for row in table.find_all("tr")[1:]:
        columns = row.find_all("td")

        if len(columns) >= 5:
            date = columns[0].get_text(strip=True)
            close = columns[4].get_text(strip=True)

            print(date, close)
else:
    print("Stock data table not found.")
