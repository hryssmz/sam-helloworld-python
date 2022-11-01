# unit/test_hello_world.py
import json

from src.functions.hello_world.app import handler
from src.tests.utils.contexts import TEST_CONTEXT
from src.tests.utils.events import TEST_EVENT


def test_handler() -> None:
    res = handler(TEST_EVENT, TEST_CONTEXT)
    assert res["statusCode"] == 200

    body = json.loads(res["body"])
    assert body["message"] == "Hello World"
