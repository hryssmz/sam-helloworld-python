#!/bin/sh
sam local invoke 'HelloWorldFunction' \
    --container-host 172.17.0.1 \
    --container-host-interface 0.0.0.0 \
    --docker-volume-basedir /home/hryssmz/docker/smz/projects/sam-python/.aws-sam/build \
    -e events/event.json
