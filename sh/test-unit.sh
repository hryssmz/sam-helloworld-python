#!/bin/sh
pytest_lambda() {
    pytest \
        --cov-report=term \
        --cov-report="html:tests/unit/$1/htmlcov" \
        --cov="functions/$1" \
        -o "pythonpath=functions/$1" \
        "tests/unit/$1" || exit 1
}

pytest_lambda hello_layer
pytest_lambda hello_module_package
pytest_lambda hello_world
