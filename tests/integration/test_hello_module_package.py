# integration/test_hello_module_package.py
import json

import requests

from tests.conftest import API_PREFIX


def test_hello_module_package() -> None:
    url = f"{API_PREFIX}/module/"
    response = requests.get(url)
    assert response.status_code == 200

    body: dict[str, str] = json.loads(response.text)
    assert "hello_module" in body
    assert "hello_package" in body
    assert body["hello_module"] == "I'm a module at /var/task/module.py!"
    assert (
        body["hello_package"]
        == "I'm a module in a package at /var/task/package/another_module.py!"
    )
