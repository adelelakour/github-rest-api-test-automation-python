import json
import requests

USER_URL = "https://api.github.com/users"
REPOS_URL = "https://api.github.com/repos"

DEFAULT_TIMEOUT = 5

def get_user(username: str):
    endpoint = f"{USER_URL}/{username}"
    response = requests.get(endpoint, timeout=DEFAULT_TIMEOUT)
    return response

def get_user_repositories(username: str):
    endpoint = f"{REPOS_URL}/{username}/ecommerce-playwright-automation-framework"

    return requests.get(
        endpoint,
        timeout=DEFAULT_TIMEOUT,
    )


repo = get_user_repositories("adelelakour")
print(json.dumps(repo.json(), indent=4))