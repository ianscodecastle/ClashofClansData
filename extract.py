import creds
import requests
import pandas as pd

headers = {
    'authorization': creds.my_key,
    'Accept': 'application/json',
}

response = requests.get('https://api.clashofclans.com/v1/players/%2380J99Y8Y', headers=headers)
user_json = response.json()
#print(user_json)

df = pd.json_normalize(user_json)
