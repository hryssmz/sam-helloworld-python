#!/bin/sh
LAYER_ROOT="layers/pip"
rm -rf ${LAYER_ROOT}/*
pip install -r layers/requirements.txt -t "${LAYER_ROOT}"
