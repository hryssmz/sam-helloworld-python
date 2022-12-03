# hello_module_package/app.py
import json
from typing import Any

from module import hello_module
from package import another_module


def handler(event: dict[str, Any], context: Any) -> dict[str, Any]:
    body = {
        "hello_module": hello_module(),
        "hello_package": another_module.hello_package(),
    }
    response = {
        "statusCode": 200,
        "headers": {},
        "body": json.dumps(body),
        "multiValueHeaders": {},
        "isBase64Encoded": False,
    }
    return response
