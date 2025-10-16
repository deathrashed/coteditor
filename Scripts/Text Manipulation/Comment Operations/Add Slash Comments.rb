#!/usr/bin/env ruby -Ku
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# Add // comments to the beginning of each selected line
# Useful for commenting out JavaScript/C++ code blocks

while $stdin.gets
    print $_.sub(/^/, "//")
end

exit
