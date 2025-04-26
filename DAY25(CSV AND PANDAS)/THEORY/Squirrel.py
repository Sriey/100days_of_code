import pandas

file = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color = file["Primary Fur Color"]
black, gray, cinnamon = 0, 0, 0

for i in color:
    if i == "Black":
        black+=1
    elif i == "Gray":
        gray+=1
    elif i == "Cinnamon":
        cinnamon+=1

print(f"Black : {black}")
print(f"gray : {gray}")
print(f"Cinnamon : {cinnamon}")
