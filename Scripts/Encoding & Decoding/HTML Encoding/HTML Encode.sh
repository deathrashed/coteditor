#!/bin/sh
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# HTML encode selected text

if [ -t 0 ] && [ -z "$(cat)" ]; then
    echo "Select text to HTML encode"
    exit 0
fi

python3 -c "
import html
import sys
text = sys.stdin.read().strip()
print(html.escape(text))
"
