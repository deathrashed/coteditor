#!/bin/sh
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# Remove line numbers from text (removes leading numbers and whitespace)

if [ -t 0 ] && [ -z "$(cat)" ]; then
    echo "Select text with line numbers to remove"
    exit 0
fi

sed 's/^[[:space:]]*[0-9]\+[[:space:]]*//'
