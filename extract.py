from unicodedata import name
import creds
import requests
import pandas as pd
from matplotlib import pyplot as plt

headers = {
    'authorization': creds.my_key,
    'Accept': 'application/json',
}

response = requests.get('https://api.clashofclans.com/v1/players/%2382UQ2G0J', headers=headers)
player_data = response.json()
#print(player_data)

df = pd.json_normalize(player_data)
df.set_index('name', inplace=True)

num_data = ['townHallLevel', 'attackWins', 'defenseWins', 'donations', 'donationsReceived', 'trophies']

player_stats = df.loc[:, num_data]
print(player_stats)
