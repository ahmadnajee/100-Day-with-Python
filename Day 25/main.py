# import csv
# from tokenize import Number

# with open("./Day 25/weather_data .csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
        


# print(temperature)

from numpy import average
import pandas

# data = pandas.read_csv("./Day 25/weather_data .csv")
# data_dict=data.to_dict()

# data_temp = data["temp"].to_list()
# print(data["temp"].max())


# Get data in rows
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]

# monday_f_temp = (monday_temp * 9/5) + 32

# print(monday_f_temp)

# data_dict = {
#     "students": ["Ahmad", "Rahmat", "Qasem","Murtaza", "Ali"],
#     "Scores": [89,90,94,100,97]
# }

# data = pandas.DataFrame(data_dict)

# print (data)

# data.to_csv("new_data.csv")

data = pandas.read_csv("./Day 25/4. 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray = data["Primary Fur Color"].value_counts()["Gray"]
black= data["Primary Fur Color"].value_counts()["Black"]
red = data["Primary Fur Color"].value_counts()["Cinnamon"]

squirrel_dict = {
    "fur color": ["Gray", "Black", "Cinnamon"],
    "count": [gray, black, red]
}

pandas.DataFrame(squirrel_dict).to_csv("squirrel_count.csv")