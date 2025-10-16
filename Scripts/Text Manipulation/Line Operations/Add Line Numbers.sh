#!/bin/sh
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# Add line numbers to each line

if [ -t 0 ] && [ -z "$(cat)" ]; then
    echo "Select text to add line numbers to"
    exit 0
fi

nl -nln
