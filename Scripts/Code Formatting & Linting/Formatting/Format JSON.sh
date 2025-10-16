#!/bin/sh
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# Format JSON text with proper indentation

if [ -t 0 ] && [ -z "$(cat)" ]; then
    echo "Select JSON text to format"
    exit 0
fi

python3 -m json.tool 2>/dev/null || echo "Error: Invalid JSON"
