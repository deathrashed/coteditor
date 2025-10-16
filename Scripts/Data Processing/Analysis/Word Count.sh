#!/bin/sh
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# Count words in selection and replace with count

if [ -t 0 ] && [ -z "$(cat)" ]; then
    echo "Select text to count words"
    exit 0
fi

wc -w | tr -d ' '
