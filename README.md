# GitHub API Testing Project

This project contains a small Python-based API testing example for the GitHub Users API. It includes:

- a simple client that fetches user data from `https://api.github.com/users/{username}`
- a JSON schema used to validate parts of the response body
- `pytest` tests that verify status codes, response fields, and key headers

## Project Structure

```text
.
├── requirements.txt
├── src
│   └── users
│       ├── schema.py
│       └── users_client.py
└── tests
    └── test_user_client.py
```

## Requirements

- Python 3.12+ recommended
- Internet access, because the tests call the live GitHub API

## Installation

Create a virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## What Is Tested

The test suite currently covers:

- existing GitHub users return `200 OK`
- a non-existing GitHub user returns `404 Not Found`
- response bodies match expected values such as `login`, `type`, `url`, and `html_url`
- important response headers are present
- GitHub rate limit headers contain valid numeric values
- the response body conforms to the schema defined in `src/users/schema.py`

The existing user scenarios currently target:

- `adelelakour`
- `elakourAdel`

## Running the Tests

```bash
python3 -m pytest -q
```

## Running the Client Script

The client module can also be executed directly:

```bash
python3 src/users/users_client.py
```

This sends a request for `adelelakour` and prints the returned JSON fields.

## Notes

- The tests depend on the live GitHub API, so failures can happen because of network issues or API rate limits.
- `src/users/users_client.py` currently performs a request and prints output at import/runtime, which is acceptable for a demo but would usually be moved behind a `main` guard in production code.
