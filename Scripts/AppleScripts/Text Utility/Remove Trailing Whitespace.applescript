(*
Remove Trailing Whitespace.applescript
Script for CotEditor

Description:
Remove trailing whitespace from all lines in the frontmost document.

written by AI Assistant
*)

--
tell application "CotEditor"
	if not (exists front document) then return
	
	tell front document
		replace for "[ \t]+$" to "" with RE and all
	end tell
end tell
