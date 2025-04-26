import requests
from datetime import datetime
import os

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
print(APP_ID,API_KEY)
NATURAL_LANGUAGE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT ="https://api.sheety.co/b0e5851166358c0d69228bf7cafa06cb/workouts/sheet1"
header = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,
}
NATURAL_LANGUAGE_PARAMS ={
    "query" : input("Tell Me Which Exercises You Did : ")
}

r1 = requests.post(url=NATURAL_LANGUAGE_ENDPOINT,json=NATURAL_LANGUAGE_PARAMS,headers=header)
data = r1.json()["exercises"]
date = datetime.today().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")
print(data)
for i in data:
    temp = {
        "sheet1":{
            "date" : date,
            "time" : time,
            "exercise" : i["name"],
            "duration" : i["duration_min"],
            "calories" : i["nf_calories"]
        }
    }
    header2 = {
        "Authorization" : "Basic c2hpd2Fuc2g6MTIzNDU2Nzg5"
    }
    r2 = requests.post(url=SHEET_ENDPOINT,json=temp,headers=header2)
    print(r2.text)