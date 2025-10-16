#!/usr/bin/env ruby -Ku
#%%%{CotEditorXInput=None}%%%
#%%%{CotEditorXOutput=InsertAfterSelection}%%%

# Insert current date and time at cursor position
# Format: YYYY-MM-DD HH:MM:SS

now = Time.now
print now.strftime("%Y-%m-%d %H:%M:%S")

exit
