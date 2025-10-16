#!/usr/bin/env ruby -Ku
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# Wrap selected text in Markdown code block with language specification
# First line should specify the language (e.g., "javascript", "python", "bash")

lines = $stdin.readlines
language = ""

if lines.length > 0
    first_line = lines[0].chomp
    if first_line.match(/^\w+$/) && lines.length > 1
        language = first_line
        lines = lines[1..-1]
    end
end

print "```#{language}\n"
lines.each do |line|
    print line
end
print "```\n"

exit
