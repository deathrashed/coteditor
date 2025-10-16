#!/bin/sh
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# Minify JSON text (remove unnecessary whitespace)

if [ -t 0 ] && [ -z "$(cat)" ]; then
    echo "Select JSON text to minify"
    exit 0
fi

python3 -c "
import json
import sys
try:
    data = json.loads(sys.stdin.read())
    print(json.dumps(data, separators=(',', ':')))
except json.JSONDecodeError as e:
    print(f'Error: {e}')
"
