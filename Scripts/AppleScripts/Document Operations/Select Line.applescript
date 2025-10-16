(*
Select Line.applescript
Script for CotEditor

Description:
Select the entire line where the cursor is positioned.

written by AI Assistant
*)

--
tell application "CotEditor"
	if not (exists front document) then return
	
	tell front document
		set selection to (contents of selection)
	end tell
end tell
