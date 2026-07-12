import pytest
from users_client import get_user


def test_existing_user():
    user_name = "adelelakour"
    response = get_user(user_name)
    assert response.status_code == 200
    response_body = response.json()

    #validate response body
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

    assert response_body["login"] == user_name
    assert response_body["id"] is None or isinstance(response_body["id"], int)
    assert response_body["type"] == "User"
    assert response_body["name"] is None or isinstance(response_body["name"], str)
    assert response_body["location"] is None or isinstance(response_body["location"], str)

    #response header validation
    header_important_fields = [
        "Date",
        "Content-Type",
        "X-RateLimit-Limit",
        "X-RateLimit-Remaining",
        "X-RateLimit-Used",
        "Content-Length",    ]

    for field in header_important_fields:
        assert field in response.headers

    rate_limit = int(response.headers["X-RateLimit-Limit"])
    remaining = int(response.headers["X-RateLimit-Remaining"])
    used = int(response.headers["X-RateLimit-Used"])

    assert rate_limit > 0
    assert 0 <= remaining <= rate_limit
    assert 0 <= used <= rate_limit

    assert "application/json" in response.headers["Content-Type"]

def test_non_existing_user():
    response = get_user("%#$#$#$#%^#$#$%#^%##!#$#@$")
    assert response.status_code == 404
    assert response.json()["message"] == 'Not Found'



