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

def total_timeseries():
    url = "https://api.covid19india.org/data.json"

    payload  = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)

    data = response.text.encode('utf8')
    data = json.loads(data)

    te = pd.json_normalize(data)  

    df = pd.DataFrame()
    totalconfirmed = []
    date = []

    for d in list(te['cases_time_series'][0]):
        date.append(d['date'])
        totalconfirmed.append(d['totalconfirmed'])
    
    df['totalconfirmed'] = totalconfirmed
    df['date'] = date

    return df



if __name__ == "__main__":
    # data = retrieve_state()
    # data2 = retrieve_total()
    data3 = total_timeseries()
    print(data3['totalconfirmed'])


        