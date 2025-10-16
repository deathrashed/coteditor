#!/bin/sh
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# Sort selected lines in reverse alphabetical order

if [ -t 0 ] && [ -z "$(cat)" ]; then
    echo "Select text to sort in reverse, or run on entire document"
    exit 0
fi

sort -r
