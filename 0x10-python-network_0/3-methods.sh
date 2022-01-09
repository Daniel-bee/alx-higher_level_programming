#!/bin/bash
# list of methods
curl -si $1 | grep "Allow" | cut -d " " -f 2-
