#!/bin/bash
# script that makes a request to 0.0.0.0:5000/catch_me
curl -sX PUT -H "Origin: You got me!" 0.0.0.0:5000/catch_me
