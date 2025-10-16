#!/bin/sh
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# Extract email addresses from selected text

if [ -t 0 ] && [ -z "$(cat)" ]; then
    echo "Select text to extract email addresses from"
    exit 0
fi

grep -oE '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' | sort | uniq
