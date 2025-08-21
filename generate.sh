#!/bin/bash

PROTO_PATH=src/proto

uv run python -m grpc_tools.protoc \
    --proto_path=$PROTO_PATH=$PROTO_PATH \
    --python_out=. \
    --pyi_out=. \
    --grpc_python_out=. \
    $PROTO_PATH/streaming.proto
