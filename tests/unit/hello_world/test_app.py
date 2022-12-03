# unit/hello_world/test.py
import json

from aws_lambda_typing.context import Context
from aws_lambda_typing.events import APIGatewayProxyEventV1

from functions.hello_world import app


def test_app(apigw_event: APIGatewayProxyEventV1, context: Context) -> None:
    response = app.handler(dict(apigw_event), context)
    assert response["statusCode"] == 200

    body: dict[str, str] = json.loads(response["body"])
    assert "message" in body
    assert body["message"] == "Hello World!"
