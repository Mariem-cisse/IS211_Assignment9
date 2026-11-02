import requests
from bs4 import BeautifulSoup
CBS NFL player touchdown statistics
url = "https://www.cbssports.com/nfl/stats/player/scoring/nfl/regular/"
headers = {
"User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
print("TOP 20 NFL TOUCHDOWN LEADERS")
for row in soup.find_all("tr")[1:21]:
print(row.get_text(" | ", strip=True))
