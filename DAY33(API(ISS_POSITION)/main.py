import requests,smtplib
from datetime import datetime,timezone
from pytz import timezone

MY_LAT = 21.82
MY_LONG = 83.84
mail = "2205932@kiit.ac.in"
password = "yusv cfry qtfs opiv"

def send_mail():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=mail, password=password)
    connection.sendmail(from_addr=mail, to_addrs="shiwanshshukla25@gmail.com", msg="SEE ABOVE TO FIND ISS.")

def utc_to_ist(utc_time_str):
    """Converts a UTC time string to IST time string."""

    utc = timezone('Europe/London')
    ist = timezone('Asia/Kolkata')
    utc_time = datetime.strptime(utc_time_str, '%Y-%m-%dT%H:%M:%S+00:00')
    utc_time = utc.localize(utc_time)
    ist_time = utc_time.astimezone(ist)
    ist_time_str = ist_time.strftime('%Y-%m-%dT%H:%M:%S+00:00')

    return ist_time_str

#Your position is within +5 or -5 degrees of the ISS position.
def check_pos(iss_lat, iss_long):
    if abs(MY_LAT - iss_lat) <= 5 and abs(MY_LONG - iss_long) <= 5:
        return True
    else:
        return False

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = (utc_to_ist(data["results"]["sunrise"]).split("T")[1].split(":")[0])
sunset = (utc_to_ist(data["results"]["sunset"]).split("T")[1].split(":")[0])

time_now = str(datetime.now()).split(" ")[1].split(":")[0]

if check_pos(iss_latitude, iss_longitude) and time_now > sunset:
    send_mail()
else:
    send_mail()




