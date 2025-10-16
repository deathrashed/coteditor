(*
Normalize Line Endings.applescript
Script for CotEditor

Description:
Convert all line endings to Unix format (LF) in the frontmost document.

written by AI Assistant
*)

--
tell application "CotEditor"
	if not (exists front document) then return
	
	tell front document
		replace for "\r\n" to "\n" with RE and all
		replace for "\r" to "\n" with RE and all
	end tell
end tell
