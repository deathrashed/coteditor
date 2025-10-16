(*
Insert Current Date.applescript
Script for CotEditor

Description:
Insert current date and time at the cursor position in the frontmost document.

written by AI Assistant
*)

--
tell application "CotEditor"
	if not (exists front document) then return
	
	set currentDateTime to (current date) as string
	
	tell front document
		set selection to currentDateTime
	end tell
end tell
