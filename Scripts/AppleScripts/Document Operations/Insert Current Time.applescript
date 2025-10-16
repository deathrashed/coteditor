(*
Insert Current Time.applescript
Script for CotEditor

Description:
Insert current time (HH:MM:SS format) at the cursor position.

written by AI Assistant
*)

--
tell application "CotEditor"
	if not (exists front document) then return
	
	set currentTime to (time string of (current date))
	
	tell front document
		set selection to currentTime
	end tell
end tell
