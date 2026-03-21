# pip3 install requests
import requests
import json

API_KEY_SECRET = "sam_konnect_default_secret"
SAM_KONNECT_URL = "https://p2p.mirotalk.com/api/v1/join"
# SAM_KONNECT_URL = "http://localhost:3000/api/v1/join"
# SAM_KONNECT_URL = "https://mirotalk.up.railway.app/api/v1/join"

headers = {
    "authorization": API_KEY_SECRET,
    "Content-Type": "application/json",
}

data = {
    "room": "test",
    "name": "mirotalk",
    "audio": "true",
    "video": "true",
    "screen": "false",
    "hide": "false",
    "notify": "true",
    "token": {
        "username": "username",
        "password": "password",
        "presenter": "true",
        "expire": "1h",
    }
}

response = requests.post(
    MIROTALK_URL,
    headers=headers,
    json=data,
)

print("Status code:", response.status_code)
data = json.loads(response.text)
print("join:", data["join"])
