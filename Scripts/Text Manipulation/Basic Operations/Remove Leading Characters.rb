#!/usr/bin/env ruby -Ku
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# Remove leading characters from each line
# Removes >, ', #, tab, space, and full-width space

while $stdin.gets
    print $_.sub(/^[>'#\t 　]/, "")
end

exit
