#!/bin/sh
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# Indent each line with 4 spaces

if [ -t 0 ] && [ -z "$(cat)" ]; then
    echo "Select text to indent"
    exit 0
fi

sed 's/^/    /'
