#!/bin/bash

logfile="./LogFile.log"

tail -n 0 -F "$logfile" | while read -r line; do
    echo "$line"
done