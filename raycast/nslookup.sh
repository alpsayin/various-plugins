#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Nslookup
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🌐
# @raycast.packageName Internet

# @raycast.argument1 { "type": "text", "placeholder": "Hostname or IP address" }
# @raycast.argument2 { "type": "text", "placeholder": "Server (optional)", "optional": true }

# Documentation:
# @raycast.description Nslookup an address
# @raycast.author Alp Sayin
# @raycast.authorURL https://github.com/alpsayin

if [ -n "$2" ]; then
    nslookup "$1" "$2"
else
    nslookup "$1"
fi
