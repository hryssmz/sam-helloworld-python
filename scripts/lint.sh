#!/bin/sh
black --quiet --check .
if [ "$?" -ne "0" ]; then
    echo "black - failed" >&2
    exit 1
else
    echo "black - passed"
fi

flake8 --quiet .
if [ "$?" -ne "0" ]; then
    echo "flake8 - failed" >&2
    exit 1
else
    echo "flake8 - passed"
fi

isort --check . >/dev/null
if [ "$?" -ne "0" ]; then
    echo "isort - failed" >&2
    exit 1
else
    echo "isort - passed"
fi

mypy . >/dev/null
if [ "$?" -ne "0" ]; then
    echo "mypy - failed" >&2
    exit 1
else
    echo "mypy - passed"
fi
