# unit/hello_module_package/test.py
import json

from aws_lambda_typing.context import Context
from aws_lambda_typing.events import APIGatewayProxyEventV1

from functions.hello_module_package import app


def test_app(apigw_event: APIGatewayProxyEventV1, context: Context) -> None:
    response = app.handler(dict(apigw_event), context)
    assert response["statusCode"] == 200

    body: dict[str, str] = json.loads(response["body"])
    assert "hello_module" in body
    assert "hello_package" in body
    assert body["hello_module"].startswith("I'm a module at /")
    assert body["hello_module"].endswith("/module.py!")
    assert body["hello_package"].startswith("I'm a module in a package at /")
    assert body["hello_package"].endswith("/package/another_module.py!")
