import json
import requests

BASE_URL = "https://api.github.com/users"
DEFAULT_TIMEOUT = 5

def get_user(username: str):
    endpoint = f"{BASE_URL}/{username}"
    response = requests.get(endpoint, timeout=DEFAULT_TIMEOUT)
    return response
