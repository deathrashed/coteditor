#!/bin/sh
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# Base64 encode selected text

if [ -t 0 ] && [ -z "$(cat)" ]; then
    echo "Select text to Base64 encode"
    exit 0
fi

base64
