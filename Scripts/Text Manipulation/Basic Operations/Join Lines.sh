#!/bin/sh
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# Join selected lines into a single line
# Lines are joined with a space separator

if [ -t 0 ] && [ -z "$(cat)" ]; then
    echo "Select text to join into a single line"
    exit 0
fi

tr '\n' ' ' | sed 's/ $//'
