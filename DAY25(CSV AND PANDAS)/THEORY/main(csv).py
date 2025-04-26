import csv

file = open("weather_data.csv", mode="r")
data = csv.reader(file)
temperature = []
for i in data:
    if i[1] != "temp":
        temperature.append(int(i[1]))
print(temperature)
file.close()