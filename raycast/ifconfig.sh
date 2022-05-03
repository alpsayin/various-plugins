#!/bin/bash

# @raycast.title Ifconfig
# @raycast.author Alp Sayin
# @raycast.authorURL https://github.com/alpsayin
# @raycast.description Ifconfig an interface.

# @raycast.icon 🌐
# @raycast.mode fullOutput
# @raycast.packageName Internet
# @raycast.schemaVersion 1

# @raycast.argument1 { "type": "text", "placeholder": "interface (optional)", "optional": true }

if [ -n "$1" ]; then
    ifconfig "$1"
else
    ifconfig
fi
