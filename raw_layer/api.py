import requests

API_BASE_URL = "http://localhost:8000"

def fetch(endpoint):
    response = requests.get(f"{API_BASE_URL}/{endpoint}")
    response.raise_for_status()
    return response.json()
