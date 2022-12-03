#!/bin/sh
LAYER_ROOT="layers/hello_world"
rm -rf ${LAYER_ROOT}/*
cp -r lib ${LAYER_ROOT}/
