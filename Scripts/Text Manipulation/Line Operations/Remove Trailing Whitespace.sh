#!/bin/sh
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# Remove trailing whitespace from each line

if [ -t 0 ] && [ -z "$(cat)" ]; then
    echo "Select text to remove trailing whitespace from"
    exit 0
fi

sed 's/[[:space:]]*$//'
