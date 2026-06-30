import requests
from app.config import BASE_URL, ACCESS_TOKEN


def get_depots():
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    response = requests.get(
        f"{BASE_URL}/depots",
        headers=headers
    )

    return response.json()


def get_vehicles():
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    response = requests.get(
        f"{BASE_URL}/vehicles",
        headers=headers
    )

    return response.json()