#!/usr/bin/env ruby -Ku
#%%%{CotEditorXInput=AllText}%%%
#%%%{CotEditorXOutput=ReplaceAllText}%%%

# Multiple find and replace operations
# First line: pattern1<TAB>replacement1<TAB>pattern2<TAB>replacement2...
# Use \1, \2, etc. for backreferences

to_find = Array.new
replace_to = Array.new

while $stdin.gets
    if $. == 1
        $_.chomp.split("\t").each_with_index do |item, i|
            if i % 2 == 0
                to_find << item
            else
                replace_to << item
            end
        end
    else
        to_find.each_with_index do |find, i|
            re_temp = Regexp.new(find)
            if replace_to[i] == nil
                replace_to[i] = ""
            else
                replace_to[i].gsub!(/\\t/, "\t")
                replace_to[i].gsub!(/\\n/, "\n")
                replace_to[i].gsub!(/\\r/, "\r")
            end
            $_.gsub!(re_temp, replace_to[i])
        end
        print $_
    end
end

exit
