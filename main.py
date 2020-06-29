import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.pyplot import figure
from active_cases import retrieve_state, retrieve_total, total_timeseries

st.title('Covid-19 in India')
st.text("")
st.text("")
st.text("")
df = st.cache(pd.read_csv)('./Data/covid_19_india.csv')

total_data = retrieve_total()
total_timeseries = total_timeseries()

x = total_timeseries['date']
y = total_timeseries['totalconfirmed']

figure(num=None, figsize=(14, 8), dpi=80, facecolor='w', edgecolor='k')
plt.xticks(rotation=45)
ax = plt.axes()
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))

plt.plot(x, y, label='Confirmed Total Cases')

plt.xlabel('Date')
plt.ylabel('No. of Cases')
plt.title(f'Detected Covid-19 Cases in India')
plt.legend()
st.pyplot()

st.text(f'''Confirmed : {total_data['confirmed']}''')
st.text(f'''Active : {total_data['active']}''')
st.text(f'''Deaths : {total_data['deaths']}''')
st.text(f'''Recovered : {total_data['recovered']}''')
        
st.markdown('## State Data')

active_data = retrieve_state()
# st.dataframe(active_data)

state = st.multiselect("Choose State", sorted(list(set(df['State/UnionTerritory']))), ["Kerala", "Delhi"])

if not state:
    st.error("Select at least one State")

is_check = st.checkbox("Display Data")

if is_check:
    for s in state:
        st.write(f'''## {s} ''')
        st.write('''### Current Data''')
     
        selected = df.loc[df['State/UnionTerritory'] == s,  ['Date', 'Confirmed', 'Deaths', 'Cured']]
        selected_active = active_data.loc[active_data['state'] == s]

        st.text(f'''Confirmed : {selected_active.confirmed.item()}''')
        st.text(f'''Active : {selected_active.active.item()}''')
        st.text(f'''Deaths : {selected_active.deaths.item()}''')
        
        # st.dataframe(selected)
        
        x = selected['Date']
        y = selected['Confirmed']
        y2 = selected['Deaths']
        y3 = selected['Cured']

        figure(num=None, figsize=(10, 6), dpi=80, facecolor='w', edgecolor='k')
        plt.xticks(rotation=45)
        ax = plt.axes()
        ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
        ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))

        plt.plot(x, y, label='Confirmed Total Cases')
        plt.plot(x, y2, label='Deaths')
        plt.plot(x, y3, label='Cured')

        plt.xlabel('Date')
        plt.ylabel('No. of Cases')
        plt.title(f'Detected Covid-19 Cases in {s}')
        plt.legend()
        st.pyplot()