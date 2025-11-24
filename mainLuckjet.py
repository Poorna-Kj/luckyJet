#Working file back up

import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta, timezone
import random

# --- TIME CONFIG (India Standard Time: UTC+5:30) ---
IST = timezone(timedelta(hours=5, minutes=30))

# URL of Lucky Jet game
url = "https://www.1win.com/games/lucky-jet"

# Send GET request
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Current IST time
    current_time = datetime.now(IST)

    # Prediction window: 4–6 minutes from now
    prediction_time_start = current_time + timedelta(minutes=4)
    prediction_time_end = current_time + timedelta(minutes=6)

    # Find prediction odds blocks
    prediction_odds = soup.find_all("div", class_="prediction-odds")

    for odd in prediction_odds:
        time = datetime.strptime(odd["time"], "%H:%M").replace(tzinfo=IST)
        odds = float(odd["odds"])

        # Filter predictions >=2.0 and in the next 4–6 minutes
        if prediction_time_start <= time <= prediction_time_end and odds >= 2.0:
            print("⚜ Signal Found")
            print("⏱ Time:", time.strftime("%I:%M:%S %p"))  # 👈 ADDED SECONDS
            print("✖ Coefficient:", odds)

# --- RANDOM GENERATION SECTION ---
current_ist = datetime.now(IST)

# Random add 5–7 minutes
random_minutes = random.randint(5, 7)
adjusted_time = current_ist + timedelta(minutes=random_minutes)

# Random coefficient
coefficientNumber = round(random.uniform(2.0, 10.01), 2)
halfNumber = round(coefficientNumber / 2, 2)
fiability = round(halfNumber / 2, 2)

# Define time prediction text
if 1.3 <= fiability <= 3.0:
    time_prediction = "3 to 5 minutes later"
elif 3.0 < fiability <= 6.5:
    time_prediction = "5 to 7 minutes later"
else:
    time_prediction = "Undetermined"

print("\n↡↠  LUCKY JET  ↞↡")
print("────────────────────────")
print("★ Time:", adjusted_time.strftime("%I:%M:%S %p"))  # 👈 ADDED SECONDS
print("★ Coefficient:", coefficientNumber)
print("★ Reliability:", halfNumber, "X+")
print("────────────────────────")
print("Prediction Time:", time_prediction)
