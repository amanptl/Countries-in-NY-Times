import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

%matplotlib notebook
df = pd.read_csv('ny_times_countries_2000_2016.csv')
df = df.set_index(['year'])

df_india = pd.DataFrame(df[df.country == 'India'])
df_china = pd.DataFrame(df[df.country == 'China'])
df_south_korea = pd.DataFrame(df[df.country == 'South Korea'])
df_japan = pd.DataFrame(df[df.country == 'Japan'])


plt.figure()
plt.plot(df_india.index, df_india['num occurrences'], label = 'India')
plt.plot(df_china.index, df_china['num occurrences'], label = 'China')
plt.plot(df_south_korea.index, df_south_korea['num occurrences'], label = 'South Korea')
plt.plot(df_japan.index, df_japan['num occurrences'], label = 'Japan')
plt.legend();
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.legend(frameon = False)
plt.xlabel('Year')
plt.ylabel('Number of Occurrences')
plt.title('New York Times and Countries')
plt.show()
