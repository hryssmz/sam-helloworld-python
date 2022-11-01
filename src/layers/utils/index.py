# layers/utils/index.py
import requests


def get_global_ip() -> str:
    res = requests.get("https://ifconfig.me")
    return res.text
