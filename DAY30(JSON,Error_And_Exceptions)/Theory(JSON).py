import json

#------------------Dump Function-----------------
file = open("test.json", mode="w")

temp_dict = {
    "temp":
            {
                "value1" : "data",
                "Value2" : "data"
            }
    }
json.dump(temp_dict, file, indent=4)
file.close()

#-------------------Load Function----------------
file = open("test.json", mode="r")

temp = json.load(file)
print(temp)
print(type(temp))
file.close()

#-------------------Update Function--------------
#[Note : Here we cannot open file directly in write mode as load doesn't support it]
with open("test.json", mode="r") as file:
    temp = {
        "temp2":
            {
                "a":"b"
            }
        }
    data = json.load(file)
    data.update(temp)

with open("test.json", mode="w") as file:
    json.dump(data, file, indent=4)