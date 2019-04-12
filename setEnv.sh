#!/usr/bin/env bash

POSTGRES_USER='demo'
POSTGRES_PASSWORD='demopassword'

# mypython bash
mypython() {
  docker run -it --rm --name tmp-python \
    -p 3000:3000 \
    -v $HOME:/root \
    -v $HOME/Projects/DevOps/python/dev:/root/bin \
    -e "PATH=${PATH}:/root/bin" \
    ppresto/python3.7 "$@"
}

#runpostgres
runpostgres() {
  docker run -d --name postgres \
    --name postgres \
    -e POSTGRES_USER=$POSTGRES_USER \
    -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD \
    -e POSTGRES_DB=sample \
    -p 80:5432 \
    -p 5432:5432 \
    --restart always \
    postgres:9.6.8-alpine "$@"
}
