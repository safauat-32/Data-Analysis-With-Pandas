"""
Different types of creating DataFrame

1.   Using CSV file
2.   Using Excel
3. From python dictonary
4. From list of tuples
5. From list of dictonaries


"""

import pandas as pd
df = pd.read_csv("weather.csv")
df

#with pyhton dictonary

weather_data = {
    'day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'temp': [12, 14, 15, 18, 20, 22, 24],
    'windspeed': [6, 7, 8, 9, 10, 11, 12],
    'event': ['Rain', 'Sunny', 'Snow', 'Rain', 'Sunny', 'Snow', 'Rain']
}
df = pd.DataFrame(weather_data)
df

#using a tuples list
weather_data = [
    ('Monday', 12, 6, 'Rain'),
    ('Tuesday', 14, 7, 'Sunny'),
    ('Wednesday', 1)
]
df = pd.DataFrame(weather_data, columns=['day', 'temp', 'windspeed', 'event'])
df

#list of disctonaries
weather_data = [
    {'day': 'Monday', 'temp': 12, 'windspeed': 6, 'event': 'Rain'},
    {'day': 'Tuesday', 'temp': 14, 'windspeed':5, 'event': 'Sunny'},
    {'day': 'Wednesday', 'windspeed':4, 'event': 'Snow'},
]
df = pd.DataFrame(weather_data)
df
