#!/bin/sh

aws lambda invoke \
    --function-name heewon-test \
    --invocation-type Event \
    response.json