# hello_world/app.py
import json
from typing import Any


def handler(event: dict[str, Any], context: Any) -> dict[str, Any]:
    body = {
        "message": "Hello World!",
    }
    response = {
        "statusCode": 200,
        "headers": {},
        "body": json.dumps(body),
        "multiValueHeaders": {},
        "isBase64Encoded": False,
    }
    return response
