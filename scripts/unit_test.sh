#!/bin/sh
pytest \
    --cov=src/functions \
    --cov-report=term \
    src/tests/unit
