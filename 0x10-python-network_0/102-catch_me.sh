#!/bin/bash
# script that makes a request to 0.0.0.0:5000/catch_me
curl -sX PUT 0.0.0.0:5000/catch_me -d "You got me!"
