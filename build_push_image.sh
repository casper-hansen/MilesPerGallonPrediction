#!/bin/bash
ADDRESS=gcr.io
PROJECT_ID=macro-authority-266522
REPOSITORY=auto
VERSION=0.17

docker build -t ${PROJECT_ID}:${VERSION} .
ID="$(docker images | grep ${REPOSITORY} | head -n 1 | awk '{print $3}')"

docker tag ${ID} $ADDRESS/${PROJECT_ID}/${REPOSITORY}:${VERSION}

docker push $ADDRESS/${PROJECT_ID}/${REPOSITORY}:${VERSION}