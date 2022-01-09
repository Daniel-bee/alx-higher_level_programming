#!/bin/bash
# list of methods
curl -siX "OPTIONS"  $1 | wc -c
