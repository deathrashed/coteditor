#!/bin/sh
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# Extract URLs from selected text

if [ -t 0 ] && [ -z "$(cat)" ]; then
    echo "Select text to extract URLs from"
    exit 0
fi

grep -oE 'https?://[^[:space:]]+' | sort | uniq
