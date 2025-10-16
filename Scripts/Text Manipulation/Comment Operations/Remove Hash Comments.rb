#!/usr/bin/env ruby -Ku
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# Remove # comments from the beginning of each selected line
# Works with the Add Hash Comments script

while $stdin.gets
    print $_.sub(/^#\s?/, "")
end

exit
