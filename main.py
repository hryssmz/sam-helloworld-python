import json

from src.functions.hello_world.app import handler
from src.tests.utils.contexts import TEST_CONTEXT
from src.tests.utils.events import TEST_EVENT


def main() -> None:
    res = handler(TEST_EVENT, TEST_CONTEXT)
    print(res["statusCode"])
    print(json.loads(res["body"]))


if __name__ == "__main__":
    main()
