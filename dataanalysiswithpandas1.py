# -*- coding: utf-8 -*-
"""Data Frame Basics

1.   Creating Dataframe
2.   Dealing with rows and columns
3.   Operations - min, max, mean, std, describe
4. Conditional selection
5. Set Index
"""

import pandas as pd

df = pd.read_csv('1901_2019_BD_weather.csv')

df

rows, columns = df.shape
rows

df.head(5)

df.tail(5)

df[2:5]

df[:]

df.columns

df['Month'] #or df.month

type(df['Month'])

df[['Year','Rain']]

df['Rain'].max()

df['Rain'].mean()

df['Rain'].min()

df['Rain'].std()

df.describe()

df[df.Rain <=40]

df[df.Rain == df.Rain.max()]

df[['Year','Month']][df.Rain == df.Rain.max()]

df.set_index('Year', inplace=True)

df

df.loc[2019]

df.reset_index(inplace=True)
