import requests
import json
import pandas as pd

def retrieve():
    url = "https://api.covidindiatracker.com/state_data.json"

    payload  = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)

    data = response.text.encode('utf8')
    data = json.loads(data)

    df = pd.json_normalize(data)
    return df

if __name__ == "__main__":
    data = retrieve()
    print(data)