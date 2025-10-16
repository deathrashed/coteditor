#!/bin/sh
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# Format CSS with proper indentation and spacing

if [ -t 0 ] && [ -z "$(cat)" ]; then
    echo "Select CSS text to beautify"
    exit 0
fi

python3 -c "
import re
import sys

def beautify_css(css):
    # Remove existing whitespace
    css = re.sub(r'\s+', ' ', css.strip())
    
    # Add line breaks and indentation
    css = re.sub(r'\{', ' {\n    ', css)
    css = re.sub(r'\}', '\n}\n', css)
    css = re.sub(r';', ';\n    ', css)
    css = re.sub(r',', ',\n', css)
    
    # Clean up extra whitespace
    css = re.sub(r'\n\s*\n', '\n', css)
    css = re.sub(r'^\s+', '', css, flags=re.MULTILINE)
    
    return css.strip()

print(beautify_css(sys.stdin.read()))
"
