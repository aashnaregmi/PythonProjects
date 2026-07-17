import pandas as pd

squirrel = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(squirrel.columns)
fur_color = squirrel["Primary Fur Color"].dropna()

final = squirrel["Primary Fur Color"].value_counts()
final.to_csv("new_data.csv")
