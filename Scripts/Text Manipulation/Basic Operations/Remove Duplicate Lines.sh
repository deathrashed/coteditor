#!/bin/sh
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# Remove duplicate lines from selection
# Preserves order of first occurrence

if [ -t 0 ] && [ -z "$(cat)" ]; then
    echo "Select text to deduplicate, or run on entire document"
    exit 0
fi

awk '!seen[$0]++'
