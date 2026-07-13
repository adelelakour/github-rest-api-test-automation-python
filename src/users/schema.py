USER_SCHEMA = {
    "type": "object",
    "required": [
        "login",
        "id",
        "url",
        "html_url",
        "type",
        "public_repos",
        "followers",
        "following",
        "name",
        "location",
    ],
    "properties": {
        "login": {"type": "string"},
        "id": {"type": "integer"},
        "url": {"type": "string"},
        "html_url": {"type": "string"},
        "type": {"type": "string"},
        "public_repos": {"type": "integer"},
        "followers": {"type": "integer"},
        "following": {"type": "integer"},
        "name": {
            "type": ["string", "null"]
        },
        "location": {
            "type": ["string", "null"]
        },
    },
}


ERROR_SCHEMA = {
    "type": "object",
    "required": [
        "message",
        "documentation_url",
    ],
    "properties": {
        "message": {
            "type": "string",
        },
        "documentation_url": {
            "type": "string",
        },
        "status": {
            "type": ["string", "integer"],
        },
    },
}