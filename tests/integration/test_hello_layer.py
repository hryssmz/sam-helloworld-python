# integration/test_hello_layer.py
import json

import pytest
import requests

from tests.conftest import API_PREFIX


@pytest.mark.skipif("_user_request_" in API_PREFIX, reason="no available")
def test_hello_layer() -> None:
    url = f"{API_PREFIX}/layer/"
    response = requests.get(url)
    assert response.status_code == 200

    body: dict[str, str] = json.loads(response.text)
    assert "hello_layer_module" in body
    assert "global_ip" in body
    assert (
        body["hello_layer_module"]
        == "I'm a layer module at /opt/python/hwl/module.py!"
    )
    assert type(body["global_ip"]) is str
