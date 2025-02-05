# IMPORTS
import requests
from datetime import datetime
import smtplib
import time
import os
from dotenv import load_dotenv

# GET ENVIRONMENT VARIABLES
load_dotenv()
my_email = os.getenv("MY_EMAIL")
my_password = os.getenv("MY_PASSWORD")
receiver = os.getenv("RECEIVER")

# ENDPOINTS AND PARAMETERS
endpoint = "https://api.sunrise-sunset.org/json"
iss_endpoint = "http://api.open-notify.org/iss-now.json"

lat = 48.563885
long = 7.772827

parameters = {"lat": lat, "lng": long, "formatted": 0}


response = requests.get(url=endpoint, params=parameters)
data = response.json()

# GETTING SUNRISE AND SUNSET TIMES
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
time_now = datetime.now()
sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
sunset_hour = int(sunset.split("T")[1].split(":")[0])

# GETTING ISS POSITION
iss_response = requests.get(url=iss_endpoint)
iss_data = iss_response.json()
my_position = (lat, long)
iss_position = (
    float(iss_data["iss_position"]["longitude"]),
    float(iss_data["iss_position"]["latitude"]),
)

# SEND AN EMAIL IF ISS CLOSE
while True:
    time.sleep(60)
    if (
        (abs(iss_position[0] - my_position[0]) < 5)
        and (abs(iss_position[1] - my_position[1]) < 5)
        and time_now.hour < sunset_hour
        and time_now > sunrise_hour
    ):
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=receiver,
                msg="Subject:Look above\n\nISS is close, watch above you",
            )
