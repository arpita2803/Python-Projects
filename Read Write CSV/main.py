# with open("weather_data.csv") as file:
#     data = file.readlines()
#
# print(data)

# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#
# print(temperature)
# import pandas as pd
# df = pd.read_csv("weather_data.csv")
# temp_list = df["temp"].to_list()

# avg_temp = sum(temp_list) / len(temp_list)
# avg_temp = df["temp"].mean()
# print(avg_temp)
#
# max_temp = df["temp"].max()
# print(max_temp)
#
# print(df.temp)
# print(df[df.day == "Monday"])
# print(df[df.temp == df.temp.max()])
# monday_data = df[df.day == "Monday"]
# temp_in_f = int(monday_data.temp) * 9/5 + 32
# print(temp_in_f)

import pandas as pd
df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
count = df["Primary Fur Color"].value_counts()
squirrel_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": count.values
}
new_df = pd.DataFrame(data=squirrel_dict)
new_df.to_csv("squirrel_count.csv")


