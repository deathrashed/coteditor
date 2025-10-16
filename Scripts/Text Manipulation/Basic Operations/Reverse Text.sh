#!/bin/sh
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# Reverse the order of lines in selection

if [ -t 0 ] && [ -z "$(cat)" ]; then
    echo "Select text to reverse"
    exit 0
fi

tac
