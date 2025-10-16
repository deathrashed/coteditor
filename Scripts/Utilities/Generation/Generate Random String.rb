#!/usr/bin/env ruby -Ku
#%%%{CotEditorXInput=None}%%%
#%%%{CotEditorXOutput=InsertAfterSelection}%%%

# Generate a random alphanumeric string
# Default length is 16 characters

length = 16
chars = ('a'..'z').to_a + ('A'..'Z').to_a + ('0'..'9').to_a
random_string = (0...length).map { chars[rand(chars.length)] }.join

print random_string

exit
