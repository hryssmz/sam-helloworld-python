# hello_layer/app.py
import json
from typing import Any

from hwl.module import hello_layer_module
from hwl.package import another_module


def handler(event: dict[str, Any], context: Any) -> dict[str, Any]:
    body = {
        "hello_layer_module": hello_layer_module(),
        "global_ip": another_module.get_global_ip(),
    }
    response = {
        "statusCode": 200,
        "headers": {},
        "body": json.dumps(body),
        "multiValueHeaders": {},
        "isBase64Encoded": False,
    }
    return response
