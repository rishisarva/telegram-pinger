import requests

RENDER_URL = "https://tarunformatter-2.onrender.com/"

try:
    r = requests.get(RENDER_URL, timeout=20)
    print("Render ping status:", r.status_code)
except Exception as e:
    print("Ping failed:", e)