#!/bin/bash
echo "Launch args: $@"

if [ "$1" == "update" ]; then
    cd /app || exit 1
    exec su user -c "bash ./update.sh"
elif [ "$1" == "cron" ]; then
    exec cron -f
else
    exec $@
fi
