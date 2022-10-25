#!/bin/bash
#displays number of bytes in location
curl -s "$1" | wc -c
