#!/bin/sh
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# Remove empty lines from selection

if [ -t 0 ] && [ -z "$(cat)" ]; then
    echo "Select text to remove empty lines from"
    exit 0
fi

grep -v '^[[:space:]]*$'
