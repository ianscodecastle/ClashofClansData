import creds
import requests
import pandas as pd

headers = {
    'authorization': creds.desktop_key,
    'Accept': 'application/json',
}

response = requests.get('https://api.clashofclans.com/v1/players/%2380J99Y8Y', headers=headers)
user_json = response.json()
#print(user_json)

df = pd.json_normalize(user_json)
player_stats = df.loc[:, ['name', 'townHallLevel', 'attackWins', 'defenseWins']]
print(player_stats)