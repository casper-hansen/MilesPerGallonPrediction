#!/bin/bash
ADDRESS=us.icr.io
NAMESPACE=mlfromscratch
REPOSITORY=auto
VERSION=0.11

docker build -t ${NAMESPACE}:${REPOSITORY} .
ID="$(docker images | grep ${REPOSITORY} | head -n 1 | awk '{print $3}')"

docker tag ${ID} ${ADDRESS}/${NAMESPACE}/${REPOSITORY}:${VERSION}

docker push ${ADDRESS}/${NAMESPACE}/${REPOSITORY}:${VERSION}