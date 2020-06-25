import pandas as pd
import altair as alt
import streamlit as st

df = pd.read_csv('./Data/covid_19_india.csv')

state = st.multiselect("Choose State", list(set(df['State/UnionTerritory'])), ["Kerala", "Delhi"])

# if not state:
#     st.error("Select at least one State")

for s in state:
    selected = df.loc[df['State/UnionTerritory'] == s]
    st.write(selected)
    data = pd.DataFrame()

    st.bar_chart(selected['Confirmed'])