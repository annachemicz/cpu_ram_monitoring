#!/bin/bash
# monitor.sh - zapisuje CPU i RAM co 10 sekund

LOGFILE=~/cpu_ram_monitor/usage.log

while true; do
    DATE=$(date '+%Y-%m-%d %H:%M:%S')
    CPU=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')
    RAM=$(free -m | awk 'NR==2{printf "%.2f", $3*100/$2 }')
    echo "$DATE CPU: $CPU% RAM: $RAM%" >> $LOGFILE
    sleep 10
done

