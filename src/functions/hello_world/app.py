# hello_world/app.py
import json
import logging

from aws_lambda_typing.context import Context
from aws_lambda_typing.events import APIGatewayProxyEventV1
from aws_lambda_typing.responses import APIGatewayProxyResponseV1

from ...layers.utils.index import get_global_ip

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(
    event: APIGatewayProxyEventV1, context: Context
) -> APIGatewayProxyResponseV1:
    logger.info("Begin execute handler")
    global_ip = get_global_ip()
    body = {
        "path": event["path"],
        "log_stream_name": context.log_stream_name,
        "message": "Hello World",
        "global_ip": global_ip,
    }
    headers = {"X-Custom-Header": "My custom value"}
    response: APIGatewayProxyResponseV1 = {
        "statusCode": 200,
        "headers": headers,
        "body": json.dumps(body),
        "multiValueHeaders": {},
        "isBase64Encoded": False,
    }
    return response
