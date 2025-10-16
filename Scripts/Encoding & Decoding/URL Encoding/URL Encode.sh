#!/bin/sh
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# URL encode selected text

if [ -t 0 ] && [ -z "$(cat)" ]; then
    echo "Select text to URL encode"
    exit 0
fi

python3 -c "
import urllib.parse
import sys
text = sys.stdin.read().strip()
print(urllib.parse.quote(text, safe=''))
"
