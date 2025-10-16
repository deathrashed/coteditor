#!/bin/sh
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# Remove 4 spaces from the beginning of each line

if [ -t 0 ] && [ -z "$(cat)" ]; then
    echo "Select text to unindent"
    exit 0
fi

sed 's/^    //'
