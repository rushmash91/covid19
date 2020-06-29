import requests
import json
import pandas as pd

def retrieve_state():
    url = "https://api.covidindiatracker.com/state_data.json"

    payload  = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)

    data = response.text.encode('utf8')
    data = json.loads(data)

    df = pd.json_normalize(data)
    return df

def retrieve_total():
    url = "https://api.covidindiatracker.com/total.json"

    payload  = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)

    data = response.text.encode('utf8')
    data = json.loads(data)

    return data

if __name__ == "__main__":
    # data = retrieve_state()
    data2 = retrieve_total()
    print(data2)