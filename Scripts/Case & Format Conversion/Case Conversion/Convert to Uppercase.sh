#!/bin/sh
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# Convert selected text to uppercase

if [ -t 0 ] && [ -z "$(cat)" ]; then
    echo "Select text to convert to uppercase"
    exit 0
fi

tr '[:lower:]' '[:upper:]'
