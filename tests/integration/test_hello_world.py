# integration/test_hello_world.py
import json

import requests

from tests.conftest import API_PREFIX


def test_hello_world() -> None:
    url = f"{API_PREFIX}/"
    response = requests.get(url)
    assert response.status_code == 200

    body: dict[str, str] = json.loads(response.text)
    assert "message" in body
    assert body["message"] == "Hello World!"
