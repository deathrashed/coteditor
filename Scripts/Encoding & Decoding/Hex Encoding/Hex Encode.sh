#!/bin/sh
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# Convert text to hexadecimal encoding

if [ -t 0 ] && [ -z "$(cat)" ]; then
    echo "Select text to convert to hex"
    exit 0
fi

xxd -p | tr -d '\n'
