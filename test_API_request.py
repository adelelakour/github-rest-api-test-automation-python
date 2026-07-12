from operator import eq

import pytest
from users_client import get_user


def test_existing_user():
    response = get_user("adelelakour")
    assert response.status_code == 200
    response_body = response.json()

    important_fields = [
        "login",
        "id",
        "url",
        "html_url",
        "type",
        "public_repos",
        "followers",
        "following",
        "created_at",
        "updated_at",
    ]
    for field in important_fields:
        assert field in response_body

    assert response_body["login"] == "adelelakour"
    assert isinstance(response_body["id"], int)
    assert response_body["type"] == "User"
    assert response_body["name"] == "A_210892_E"
    assert response_body["id"] == 133891709
    assert response_body["location"] == "Munich"

    #response header validation
    assert "application/json" in response.headers["Content-Type"]
    assert "X-RateLimit-Limit" in response.headers
    assert "X-RateLimit-Remaining" in response.headers

def test_non_existing_user():
    response = get_user("unknown_user")
    assert response.status_code == 404
    assert response.json()["message"] == 'Not Found'



