import creds
import requests
import pandas as pd
from matplotlib import pyplot as plt

headers = {
    'authorization': creds.my_key,
    'Accept': 'application/json'
}

def get_player_data():
    response = requests.get('https://api.clashofclans.com/v1/players/%2382UQ2G0J', headers=headers)
    json_response = response.json()
    #print(json_response)

    df = pd.json_normalize(json_response)
    df.set_index('name', inplace=True)

    num_data = ['townHallLevel', 'attackWins', 'defenseWins', 'donations', 'donationsReceived', 'trophies']

    player_stats = df.loc[:, num_data]
    return player_stats

def get_clan_data():
    response = requests.get('https://api.clashofclans.com/v1/clans/%238GLCP2CU/members?limit=5', headers=headers)
    json_response = response.json()['items']

    df = pd.json_normalize(json_response)
    #df.set_index('name', inplace=True)

    member_info = ['tag', 'name', 'role', 'expLevel', 'clanRank', 'donations', 'donationsReceived']
    member_stats = df.loc[:, member_info]
    
    donations = df.loc[:, ['donations', 'donationsReceived']]
    # donations.plot(x='name', kind='bar', xlabel='Clan Members', rot=0)
    # plt.show()
    return donations

# get_player_data()
# get_clan_data()