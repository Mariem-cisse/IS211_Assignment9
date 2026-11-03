
import requests
from bs4 import BeautifulSoup
import re

# CBS Sports NFL scoring statistics
url = "https://www.cbssports.com/nfl/stats/player/scoring/nfl/regular/all/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers, timeout=20)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table")

players = []

print("TOP 20 NFL TOUCHDOWN LEADERS")
print("----------------------------")

if table:
    for row in table.find_all("tr")[1:]:
        cells = row.find_all("td")

        if len(cells) < 8:
            continue

        player_info = cells[0].get_text(" ", strip=True)

        match = re.search(
            r"\b(QB|RB|WR|TE|FB|K|P)\b",
            player_info
        )

        if not match:
            continue

        position = match.group(1)
        team = player_info.split()[-1]
        player_name = player_info.split(position)[0].strip()

        touchdowns = 0

        for cell in cells[2:8]:
            value = cell.get_text(strip=True)

            if value.isdigit():
                touchdowns += int(value)

        players.append(
            (player_name, position, team, touchdowns)
        )

    players.sort(key=lambda player: player[3], reverse=True)

    print("PLAYER | POSITION | TEAM | TOUCHDOWNS")
    print("--------------------------------------")

    for player in players[:20]:
        print(f"{player[0]} | {player[1]} | {player[2]} | {player[3]}")

else:
    print("No statistics table found.")
