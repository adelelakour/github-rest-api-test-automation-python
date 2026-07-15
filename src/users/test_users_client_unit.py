from src.users.users_client import get_user


def test_get_user_returns_fake_response(monkeypatch):
    fake_response = object()

    def fake_get(url, timeout):
        return fake_response

    monkeypatch.setattr(
        "src.users.users_client.requests.get",
        fake_get,
    )

    actual_response = get_user("octocat")

    assert actual_response is fake_response

