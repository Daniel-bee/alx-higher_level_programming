#!/bin/bash
# JSON POST request to a URL passed as the first argument
curl -sH $1 "Content-Type: application/json" -d @$s2
