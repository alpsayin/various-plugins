#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Dig
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🌐
# @raycast.packageName Internet

# @raycast.argument1 { "type": "text", "placeholder": "Hostname or IP address" }
# @raycast.argument2 { "type": "text", "placeholder": "Server (optional)", "optional": true }

# Documentation:
# @raycast.description Dig an address
# @raycast.author Alp Sayin
# @raycast.authorURL https://github.com/alpsayin

if [ -n "$2" ]; then
    dig "$1" "@$2"
else
    dig "$1"
fi
