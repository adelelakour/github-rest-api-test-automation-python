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
        "created_at",
        "updated_at",
    ],
    "properties": {
        "login": {"type": "string"},
        "id": {"type": "integer"},
        "type": {"type": "string"},
        "name": {
            "type": ["string", "null"]
        },
        "location": {
            "type": ["string", "null"]
        },
    },
}