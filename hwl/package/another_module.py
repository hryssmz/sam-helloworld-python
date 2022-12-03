# hwl/package/another_module.py
import requests


def get_global_ip() -> str:
    response = requests.get("http://ifconfig.me")
    return response.text
