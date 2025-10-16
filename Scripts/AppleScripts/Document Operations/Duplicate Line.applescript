(*
Duplicate Line.applescript
Script for CotEditor

Description:
Duplicate the current line at the cursor position.

written by AI Assistant
*)

--
tell application "CotEditor"
	if not (exists front document) then return
	
	tell front document
		set currentLine to contents of selection
		set selection to currentLine & "\n" & currentLine
	end tell
end tell
