# unit/hello_layer/test_app.py
import json

from aws_lambda_typing.context import Context
from aws_lambda_typing.events import APIGatewayProxyEventV1

from functions.hello_layer import app


def test_app(apigw_event: APIGatewayProxyEventV1, context: Context) -> None:
    response = app.handler(dict(apigw_event), context)
    assert response["statusCode"] == 200

    body: dict[str, str] = json.loads(response["body"])
    assert "hello_layer_module" in body
    assert "global_ip" in body
    assert body["hello_layer_module"].startswith("I'm a layer module at /")
    assert body["hello_layer_module"].endswith("/hwl/module.py!")
    assert type(body["global_ip"]) is str
