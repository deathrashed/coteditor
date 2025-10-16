#!/bin/sh
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# Sort selected lines alphabetically
# If no selection, sorts all lines

if [ -t 0 ] && [ -z "$(cat)" ]; then
    # No input, just show usage
    echo "Select text to sort, or run on entire document"
    exit 0
fi

sort
