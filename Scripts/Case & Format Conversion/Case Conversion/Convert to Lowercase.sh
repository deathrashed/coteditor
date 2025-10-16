#!/bin/sh
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# Convert selected text to lowercase

if [ -t 0 ] && [ -z "$(cat)" ]; then
    echo "Select text to convert to lowercase"
    exit 0
fi

tr '[:upper:]' '[:lower:]'
