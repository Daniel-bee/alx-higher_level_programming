#!/bin/bash
# script that makes a request to 0.0.0.0:5000/catch_me
curl -sLX PUT -d "You got me!" 0.0.0.0:5000/catch_me
