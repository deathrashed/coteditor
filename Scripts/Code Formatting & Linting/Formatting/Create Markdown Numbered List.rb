#!/usr/bin/env ruby -Ku
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# Convert selected text to Markdown numbered list
# Each line becomes a numbered list item

counter = 1
while $stdin.gets
    line = $_.chomp
    unless line.empty?
        print "#{counter}. " + line + "\n"
        counter += 1
    else
        print "\n"
    end
end

exit
