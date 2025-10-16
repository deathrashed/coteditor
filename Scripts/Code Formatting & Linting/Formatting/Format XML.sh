#!/bin/sh
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# Format XML text with proper indentation

if [ -t 0 ] && [ -z "$(cat)" ]; then
    echo "Select XML text to format"
    exit 0
fi

xmllint --format - 2>/dev/null || echo "Error: Invalid XML or xmllint not found"
