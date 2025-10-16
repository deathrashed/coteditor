#!/bin/sh
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# HTML decode selected text

if [ -t 0 ] && [ -z "$(cat)" ]; then
    echo "Select text to HTML decode"
    exit 0
fi

python3 -c "
import html
import sys
text = sys.stdin.read().strip()
print(html.unescape(text))
"
