#!/bin/bash
# JSON POST request to a URL passed as the first argument
curl -sH "Content-Type: application/json" -d @$s2 $1
