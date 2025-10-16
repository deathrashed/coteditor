(*
Convert Spaces to Tabs.applescript
Script for CotEditor

Description:
Convert 4 consecutive spaces to tab characters in the frontmost document.

written by AI Assistant
*)

--
tell application "CotEditor"
	if not (exists front document) then return
	
	tell front document
		replace for "    " to "\t" with RE and all
	end tell
end tell
