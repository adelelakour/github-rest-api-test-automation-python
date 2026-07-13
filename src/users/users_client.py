import json
import requests


def get_user(username: str):
    resource_url = "https://api.github.com/users"
    endpoint = f"{resource_url}/{username}"
    return requests.get(endpoint)


response_body = get_user("adelelakour")
for line in response_body.json():
    print (f" {line} : {response_body.json()[line]}")
# print(json.dumps(response_body.json(), indent=4))

