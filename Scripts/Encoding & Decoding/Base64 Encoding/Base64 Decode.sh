#!/bin/sh
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# Base64 decode selected text

if [ -t 0 ] && [ -z "$(cat)" ]; then
    echo "Select text to Base64 decode"
    exit 0
fi

base64 -d
