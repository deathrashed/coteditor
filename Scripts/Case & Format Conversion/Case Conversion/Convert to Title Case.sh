#!/bin/sh
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# Convert selected text to title case (first letter of each word capitalized)

if [ -t 0 ] && [ -z "$(cat)" ]; then
    echo "Select text to convert to title case"
    exit 0
fi

sed 's/\b\w/\U&/g'
