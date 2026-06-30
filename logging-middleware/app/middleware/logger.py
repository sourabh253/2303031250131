import requests
from app.config.settings import BASE_URL, ACCESS_TOKEN


def Log(stack, level, package, message):
    url = f"{BASE_URL}/logs"

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    body = {
        "stack": stack,
        "level": level,
        "package": package,
        "message": message
    }

    response = requests.post(url, json=body, headers=headers)

    print("Status Code:", response.status_code)
    print("Response:", response.text)

    return response