#!/bin/bash
# JSON POST request to a URL passed as the first argument
curl -sX $1 POST -H "Content-Type: application/json" -d @$s2
