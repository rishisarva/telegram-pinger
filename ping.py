import os
import requests
import time

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

payload = {
    "chat_id": CHAT_ID,
    "text": "ping"
}

success = False

for attempt in range(5):  # 5 retries
    try:
        r = requests.post(url, json=payload, timeout=20)
        print("Status:", r.status_code)
        print("Response:", r.text)

        if r.status_code == 200:
            success = True
            print("Ping sent successfully")
            break
    except Exception as e:
        print("Attempt failed:", e)

    time.sleep(10)

if not success:
    print("Giving up, but NOT failing the workflow")