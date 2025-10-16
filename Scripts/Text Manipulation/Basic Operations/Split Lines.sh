#!/bin/sh
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# Split selected text into separate lines
# Splits on spaces, commas, and semicolons

if [ -t 0 ] && [ -z "$(cat)" ]; then
    echo "Select text to split into lines"
    exit 0
fi

tr ',;' '\n' | tr ' ' '\n' | grep -v '^$'
