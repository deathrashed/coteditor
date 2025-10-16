#!/usr/bin/env ruby -Ku
#%%%{CotEditorXInput=Selection}%%%
#%%%{CotEditorXOutput=ReplaceSelection}%%%

# Wrap selected text in curly braces {}
# Ignores empty lines at the beginning and end

a = $stdin.read

soa = ""
eoa = ""

if /\A([\n\r]+)/ =~ a
    soa = $1
    a.sub!(/\A[\n\r]+/, "")
end
if /([\n\r]+)\Z/ =~ a
    eoa = $1
    a.sub!(/[\n\r]+\Z/, "")
end

print(soa+"{"+a+"}"+eoa)

exit
