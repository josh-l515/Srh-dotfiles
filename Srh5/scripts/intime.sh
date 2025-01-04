#!/bin/bash

# Countdown target date and time (YYYY-MM-DD HH:MM:SS)
TARGET_DATE="2025-01-01 00:00:00"

# Current date and time
CURRENT_DATE=$(date +"%Y-%m-%d %H:%M:%S")

# Calculate the difference in seconds
DIFF=$(($(date -d "$TARGET_DATE" +%s) - $(date -d "$CURRENT_DATE" +%s)))

# Ensure we don't go negative
if [ $DIFF -lt 0 ]; then
  echo "00-00-00-00-00-00"
  exit 0
fi

# Conversion factors
SECONDS_IN_YEAR=$((365 * 24 * 60 * 60)) # Approximate (ignoring leap years)
SECONDS_IN_WEEK=$((7 * 24 * 60 * 60))
SECONDS_IN_DAY=$((24 * 60 * 60))
SECONDS_IN_HOUR=$((60 * 60))
SECONDS_IN_MINUTE=60

# Years, weeks, days, hours, minutes, and seconds
YEARS=$((DIFF / SECONDS_IN_YEAR))
DIFF=$((DIFF % SECONDS_IN_YEAR))

WEEKS=$((DIFF / SECONDS_IN_WEEK))
DIFF=$((DIFF % SECONDS_IN_WEEK))

DAYS=$((DIFF / SECONDS_IN_DAY))
DIFF=$((DIFF % SECONDS_IN_DAY))

HOURS=$((DIFF / SECONDS_IN_HOUR))
DIFF=$((DIFF % SECONDS_IN_HOUR))

MINUTES=$((DIFF / SECONDS_IN_MINUTE))
SECONDS=$((DIFF % SECONDS_IN_MINUTE))

# Format as 00·00·00·00·00·00
printf "%02d·%02d·%02d·%02d·%02d·%02d\n" $YEARS $WEEKS $DAYS $HOURS $MINUTES $SECONDS
