
'''# **Reading writing CSV files**


1.   Read CSV
2.   Write CSV
3. Read Excel
4. Write excel

'''


import pandas as pd
df = pd.read_csv("stock.csv")
df

df = pd.read_csv("stock.csv", skiprows=1)
df

df = pd.read_csv("stock.csv", header=2)
df

df = pd.read_csv("stock.csv", header= None, names=["ticker", "eps", "revenue", "price", "people"])
df

df = pd.read_csv("stock.csv",nrows = 4)
df

df = pd.read_csv("stock.csv", na_values = ['not available', 'na'])
df

df = pd.read_csv("stock.csv", na_values = {
    'eps': ['not available', 'na'],
    'revenue': ['not available', 'na', -1],
    'people': ['not available', 'na']
})
df

#This allows us to do data munging and data wrangling

df.to_csv('new.csv')

df.to_csv('new.csv', index=False)

df.columns

df.to_csv("new.csv",columns = ['tickers','eps'])

df.to_csv("new.csv",header = False)

"""Excel File"""

df = pd.read_excel("stock.xlsx")
df

#converting messy data into something meaningfull
def convert_people_cell(cell):
  if cell =='na':
    return 'sam walton'
  return cell

df = pd.read_excel("stock.xlsx", converters ={
    'people': convert_people_cell
})
df

#writing in excel file
df.to_excel("new.xlsx", sheet_name="stocks")

df.to_excel("new.xlsx", sheet_name="stocks", index=False)
