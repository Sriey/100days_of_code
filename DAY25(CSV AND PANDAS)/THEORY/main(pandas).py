import pandas

data = pandas.read_csv("weather_data.csv")
print(data)

temp = data["temp"].to_list()
print(round(sum(temp) / len(temp), 3))

#--------------------OR---------------------

print(data["temp"].mean())

#-------------------MAX----------------------

print(data["temp"].max())

#-------------GET COLUMN---------------------

print(data["temp"])

#--------------GET ROW-----------------------

monday = data[data.day == "Monday"]
print(monday.condition)
monday_temp = int(monday.temp)
print((monday_temp*9/5)+32)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")