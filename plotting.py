import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(('./Data/covid_19_india.csv'))
s = input('State ')
selected = df.loc[df['State/UnionTerritory'] == s, ['Date', 'Confirmed', 'Deaths', 'Cured']]

x = selected['Date']
y = selected['Confirmed']
y2 = selected['Deaths']
y3 = selected['Cured']

plt.plot(x, y)
plt.plot(x, y2)
plt.plot(x, y3)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph')
plt.legend()
plt.show()