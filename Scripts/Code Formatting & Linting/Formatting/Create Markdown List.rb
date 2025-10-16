#!/usr/bin/env ruby -Ku
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# Convert selected text to Markdown unordered list
# Each line becomes a list item with - prefix

while $stdin.gets
    line = $_.chomp
    unless line.empty?
        print "- " + line + "\n"
    else
        print "\n"
    end
end

exit
