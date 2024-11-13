#!/bin/bash

hpfeeds-broker -e tcp:port=20000 --exporter=0.0.0.0:9431 --auth=./auth/users.json --debug --name="broker_a"
