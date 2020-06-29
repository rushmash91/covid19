import pandas as pd
import altair as alt
import streamlit as st
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.pyplot import figure
from active_cases import retrieve

df = st.cache(pd.read_csv)('./Data/covid_19_india.csv')

state = st.multiselect("Choose State", list(set(df['State/UnionTerritory'])), ["Kerala", "Delhi"])

# if not state:
#     st.error("Select at least one State")
is_check = st.checkbox("Display Data")
if is_check:
    for s in state:
        st.write(f'''## {s} ''')
        selected = df.loc[df['State/UnionTerritory'] == s,  ['Date', 'Confirmed', 'Deaths', 'Cured']]
        st.dataframe(selected)
        
        x = selected['Date']
        y = selected['Confirmed']
        y2 = selected['Deaths']
        y3 = selected['Cured']

        figure(num=None, figsize=(10, 6), dpi=80, facecolor='w', edgecolor='k')
        plt.xticks(rotation=45)
        ax = plt.axes()
        ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
        ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))

        plt.plot(x, y, label='Confirmed New Cases')
        plt.plot(x, y2, label='Deaths')
        plt.plot(x, y3, label='Cured')

        plt.xlabel('Date')
        plt.ylabel('No. of Cases')
        plt.title(f'Detected Covid-19 Cases in {s}')
        plt.legend()
        st.pyplot()