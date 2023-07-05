#!/bin/bash

logfile="./LogFile.log"

KAFKA_BROKER="PLAINTEXT://kafka:29092"
KAFKA_TOPIC="MSGS"

tail -n 0 -F "$logfile" | while read -r line; do
    kafkacat -b "$KAFKA_BROKER" -t "$KAFKA_TOPIC" -P <<< "$line"
    echo "$line"
done
