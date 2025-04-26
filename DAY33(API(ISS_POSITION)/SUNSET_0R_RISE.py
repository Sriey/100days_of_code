import requests
from datetime import datetime,timezone
from pytz import timezone

def utc_to_ist(utc_time_str):
    """Converts a UTC time string to IST time string."""

    # Define timezones
    utc = timezone('Europe/London')
    ist = timezone('Asia/Kolkata')

    # Parse the UST time string
    utc_time = datetime.strptime(utc_time_str, '%Y-%m-%dT%H:%M:%S+00:00')

    # Localize the UST time to the UST timezone
    utc_time = utc.localize(utc_time)

    # Convert to IST
    ist_time = utc_time.astimezone(ist)

    # Format the IST time as a string
    ist_time_str = ist_time.strftime('%Y-%m-%dT%H:%M:%S+00:00')

    return ist_time_str

parameter = {
    "lat" : 21.826431004771177,
    "lng" : 83.84794720976967,
    "formatted" : 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameter)

response.raise_for_status()
data = response.json()


print("sunrise :", utc_to_ist(data["results"]["sunrise"]).split("T")[1])
print("sunset :", utc_to_ist(data["results"]["sunset"]).split("T")[1])
