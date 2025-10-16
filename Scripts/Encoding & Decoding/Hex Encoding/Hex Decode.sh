#!/bin/sh
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# Convert hexadecimal back to text

if [ -t 0 ] && [ -z "$(cat)" ]; then
    echo "Select hex text to decode"
    exit 0
fi

xxd -r -p
