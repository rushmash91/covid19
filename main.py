import pandas as pd
import altair as alt
import streamlit as st

df = pd.read_csv('./Data/covid_19_india.csv')

state = st.multiselect("Choose State", list(set(df['State/UnionTerritory'])), ["Kerala", "Delhi"])

# if not state:
#     st.error("Select at least one State")

for s in state:
    st.write(f'''## {s} ''')
    selected = df.loc[df['State/UnionTerritory'] == s, ['Date', 'Confirmed']]
    st.write(selected)
    selected = selected.rename(columns={'Date':'index'}).set_index('index')
    st.write(selected)
    st.bar_chart(selected)