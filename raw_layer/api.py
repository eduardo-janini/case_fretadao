import requests

API_BASE_URL = "http://localhost:8000"

def fetch(endpoint, params=None):
    response = requests.get(
        f"{API_BASE_URL}/{endpoint}",
        params=params
    )
    response.raise_for_status()
    return response.json()
