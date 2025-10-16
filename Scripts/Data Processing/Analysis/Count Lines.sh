#!/bin/sh
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# Count lines in selection and replace with count

if [ -t 0 ] && [ -z "$(cat)" ]; then
    echo "Select text to count lines"
    exit 0
fi

wc -l | tr -d ' '
